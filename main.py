from __future__ import annotations

import base64
import io
import json
import time
import uuid
from functools import lru_cache
from pathlib import Path
from typing import Any

import cv2
import numpy as np
import torch
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from PIL import Image
from torchvision import models, transforms

from disease_details import DISEASE_INFO, get_disease_info
from GradCamImplementation import GradCAM


BASE_DIR = Path(__file__).resolve().parent
UI_FILE = BASE_DIR / "ui_mockup.html"
SAVED_MODELS_DIR = BASE_DIR / "Saved Models"
METADATA_FILE = SAVED_MODELS_DIR / "models_metadata.json"
MAX_UPLOAD_BYTES = 10 * 1024 * 1024

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_FILES = {
    "resnet50": {
        "display_name": "ResNet-50",
        "directory": SAVED_MODELS_DIR / "ResNet50",
        "weights": "resnet50_weights.pth",
        "scripted": "resnet50_scripted.pt",
        "badge": "High Accuracy",
    },
    "mobilenet_v2": {
        "display_name": "MobileNetV2",
        "directory": SAVED_MODELS_DIR / "MobileNetV2",
        "weights": "mobilenet_v2_weights.pth",
        "scripted": "mobilenet_v2_scripted.pt",
        "badge": "Fast",
    },
}


app = FastAPI(title="PhytoScan AI", version="2.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def load_metadata() -> dict[str, Any]:
    if not METADATA_FILE.exists():
        raise RuntimeError(f"Model metadata file not found: {METADATA_FILE}")
    return json.loads(METADATA_FILE.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def metadata() -> dict[str, Any]:
    return load_metadata()


def idx_to_class(model_id: str) -> dict[int, str]:
    class_to_idx = metadata()[model_id]["class_to_idx"]
    return {idx: name for name, idx in class_to_idx.items()}


def display_class_name(class_name: str) -> dict[str, str]:
    if "___" not in class_name:
        label = class_name.replace("_", " ")
        return {"plant": "Unknown", "disease": label, "label": label}

    plant, disease = class_name.split("___", 1)
    plant = plant.replace("_", " ").replace(",", ", ")
    disease = disease.replace("_", " ")
    return {"plant": plant, "disease": disease, "label": f"{plant} - {disease}"}


def extract_state_dict(checkpoint: Any) -> dict[str, torch.Tensor]:
    if isinstance(checkpoint, dict):
        for key in ("model_state_dict", "state_dict", "model", "net"):
            value = checkpoint.get(key)
            if isinstance(value, dict):
                checkpoint = value
                break

    if not isinstance(checkpoint, dict):
        raise RuntimeError("Checkpoint does not contain a PyTorch state dict.")

    state_dict = {}
    for key, value in checkpoint.items():
        if not torch.is_tensor(value):
            continue
        clean_key = key
        for prefix in ("module.", "model."):
            if clean_key.startswith(prefix):
                clean_key = clean_key[len(prefix) :]
        state_dict[clean_key] = value
    return state_dict


def build_torchvision_model(model_id: str, num_classes: int) -> torch.nn.Module:
    if model_id == "resnet50":
        model = models.resnet50(weights=None)
        model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
        return model

    if model_id == "mobilenet_v2":
        model = models.mobilenet_v2(weights=None)
        model.classifier[1] = torch.nn.Linear(model.classifier[1].in_features, num_classes)
        return model

    raise ValueError(f"Unsupported model id: {model_id}")


def load_weight_model(model_id: str) -> torch.nn.Module:
    model_meta = metadata()[model_id]
    config = MODEL_FILES[model_id]
    model = build_torchvision_model(model_id, model_meta["num_classes"])
    weights_path = config["directory"] / config["weights"]

    if not weights_path.exists():
        raise FileNotFoundError(weights_path)

    checkpoint = torch.load(weights_path, map_location=DEVICE)
    state_dict = extract_state_dict(checkpoint)
    current_state = model.state_dict()
    compatible_state = {
        key: value
        for key, value in state_dict.items()
        if key in current_state and tuple(value.shape) == tuple(current_state[key].shape)
    }
    if not compatible_state:
        raise RuntimeError(f"No compatible tensors found in {weights_path}")

    model.load_state_dict(compatible_state, strict=False)
    model.to(DEVICE)
    model.eval()
    return model


def load_scripted_model(model_id: str) -> torch.nn.Module:
    config = MODEL_FILES[model_id]
    scripted_path = config["directory"] / config["scripted"]
    if not scripted_path.exists():
        raise FileNotFoundError(scripted_path)

    model = torch.jit.load(str(scripted_path), map_location=DEVICE)
    model.to(DEVICE)
    model.eval()
    return model


@lru_cache(maxsize=2)
def model_bundle(model_id: str) -> dict[str, Any]:
    if model_id not in MODEL_FILES:
        raise HTTPException(status_code=404, detail=f"Unknown model '{model_id}'")

    try:
        model = load_weight_model(model_id)
        load_source = "weights"
    except Exception:
        model = load_scripted_model(model_id)
        load_source = "scripted"

    model_meta = metadata()[model_id]
    return {
        "id": model_id,
        "model": model,
        "load_source": load_source,
        "meta": model_meta,
        "idx_to_class": idx_to_class(model_id),
        "transform": transforms.Compose(
            [
                transforms.Resize((model_meta["image_size"], model_meta["image_size"])),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=model_meta["imagenet_mean"],
                    std=model_meta["imagenet_std"],
                ),
            ]
        ),
    }


def get_gradcam_target_layer(model_id: str, model: torch.nn.Module) -> torch.nn.Module:
    if model_id == "resnet50" and hasattr(model, "layer4"):
        return model.layer4[-1]
    if model_id == "mobilenet_v2" and hasattr(model, "features"):
        return model.features[-1]

    candidates = [
        module
        for _, module in model.named_modules()
        if isinstance(module, (torch.nn.Conv2d, torch.nn.BatchNorm2d))
    ]
    if not candidates:
        raise RuntimeError("Could not find a target layer for Grad-CAM.")
    return candidates[-1]


def image_to_data_url(image: Image.Image, image_format: str = "JPEG") -> str:
    buffer = io.BytesIO()
    image.save(buffer, format=image_format)
    mime = "image/png" if image_format.upper() == "PNG" else "image/jpeg"
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def make_gradcam_overlay(bundle: dict[str, Any], image: Image.Image, tensor: torch.Tensor, class_idx: int) -> str:
    model = bundle["model"]
    target_layer = get_gradcam_target_layer(bundle["id"], model)
    cam = GradCAM(model, target_layer, bundle["idx_to_class"])
    try:
        heatmap, _, _, _ = cam.generate(tensor.clone(), target_class=class_idx)
    finally:
        cam.remove_hooks()

    size = bundle["meta"]["image_size"]
    base = np.array(image.resize((size, size))).astype(np.uint8)
    heatmap_uint8 = np.uint8(255 * heatmap)
    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
    heatmap_color = cv2.cvtColor(heatmap_color, cv2.COLOR_BGR2RGB)
    overlay = cv2.addWeighted(base, 0.45, heatmap_color, 0.55, 0)
    return image_to_data_url(Image.fromarray(overlay), "JPEG")


def treatment_payload(class_name: str) -> dict[str, Any]:
    info = get_disease_info(class_name)
    if "error" in info:
        return {
            "available": False,
            "class_name": class_name,
            "disease_name": display_class_name(class_name)["disease"],
            "pathogen": "Unknown",
            "pathogen_type": "Unknown",
            "severity": {"level": 0, "label": "Unknown", "description": ""},
            "treatment": {
                "immediate_actions": ["No treatment guide is available for this class."],
                "chemical_treatment": [],
                "cultural_practices": [],
            },
        }

    return {
        "available": True,
        "class_name": class_name,
        "disease_name": info["disease_name"],
        "pathogen": info["pathogen"],
        "pathogen_type": info["pathogen_type"],
        "severity": info["severity"],
        "description": info["description"],
        "treatment": info["treatment"],
    }


@app.get("/")
def index() -> FileResponse:
    return FileResponse(UI_FILE)


@app.get("/api/models")
def models_list() -> JSONResponse:
    data = []
    for model_id, config in MODEL_FILES.items():
        model_meta = metadata()[model_id]
        data.append(
            {
                "id": model_id,
                "name": config["display_name"],
                "num_classes": model_meta["num_classes"],
                "image_size": model_meta["image_size"],
                "best_val_acc": model_meta["best_val_acc"],
                "best_epoch": model_meta["best_epoch"],
                "badge": config["badge"],
            }
        )
    return JSONResponse({"models": data})


@app.get("/api/treatment/{class_name}")
def treatment(class_name: str) -> JSONResponse:
    return JSONResponse(treatment_payload(class_name))


@app.post("/api/predict")
async def predict(
    file: UploadFile = File(...),
    model_name: str = Form("resnet50"),
    confidence_threshold: float = Form(0.75),
    include_gradcam: bool = Form(True),
) -> JSONResponse:
    if model_name not in MODEL_FILES:
        raise HTTPException(status_code=400, detail=f"Unsupported model '{model_name}'")

    raw = await file.read()
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="Image exceeds the 10MB upload limit.")

    try:
        image = Image.open(io.BytesIO(raw)).convert("RGB")
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Upload must be a valid JPG, PNG, or WEBP image.") from exc

    bundle = model_bundle(model_name)
    tensor = bundle["transform"](image).unsqueeze(0).to(DEVICE)

    start = time.perf_counter()
    with torch.no_grad():
        logits = bundle["model"](tensor)
        probabilities = torch.nn.functional.softmax(logits, dim=1)[0]
    inference_ms = round((time.perf_counter() - start) * 1000, 1)

    top_values, top_indices = torch.topk(probabilities, k=min(5, probabilities.numel()))
    top_predictions = []
    for rank, (value, index) in enumerate(zip(top_values.tolist(), top_indices.tolist()), start=1):
        class_name = bundle["idx_to_class"].get(index, "unknown")
        display = display_class_name(class_name)
        top_predictions.append(
            {
                "rank": rank,
                "class_index": index,
                "class_name": class_name,
                "plant": display["plant"],
                "disease": display["disease"],
                "label": display["label"],
                "confidence": round(value * 100, 2),
                "probability": value,
            }
        )

    top = top_predictions[0]
    healthy = top["class_name"].lower().endswith("healthy")
    above_threshold = top["probability"] >= confidence_threshold

    gradcam_data_url = None
    gradcam_error = None
    if include_gradcam:
        try:
            gradcam_data_url = make_gradcam_overlay(bundle, image, tensor, top["class_index"])
        except Exception as exc:
            gradcam_error = str(exc)

    response = {
        "specimen_id": f"SP-{uuid.uuid4().hex[:8].upper()}",
        "model": {
            "id": model_name,
            "name": MODEL_FILES[model_name]["display_name"],
            "load_source": bundle["load_source"],
            "num_classes": bundle["meta"]["num_classes"],
        },
        "status": {
            "healthy": healthy,
            "above_threshold": above_threshold,
            "label": "Healthy" if healthy else ("Disease Detected" if above_threshold else "Review Needed"),
        },
        "threshold": confidence_threshold,
        "inference_ms": inference_ms,
        "image": image_to_data_url(image),
        "gradcam": gradcam_data_url,
        "gradcam_error": gradcam_error,
        "top_prediction": top,
        "top_predictions": top_predictions,
        "treatment": treatment_payload(top["class_name"]),
    }
    return JSONResponse(response)
