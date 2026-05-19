import cv2
import numpy as np
import torch


idx_to_class = {}


class GradCAM:
    """
    Gradient-weighted Class Activation Mapping (Grad-CAM).

    Produces a coarse localization heatmap highlighting the regions
    of an input image that are most important for a given prediction.

    Args:
        model: A PyTorch CNN model (already on DEVICE, in eval mode)
        target_layer: The convolutional layer to hook into
                      (e.g., model.features[-1] for MobileNetV2,
                       model.layer4[-1] for ResNet50)
    """

    def __init__(self, model, target_layer, class_names=None):
        self.model = model
        self.target_layer = target_layer
        self.class_names = class_names or idx_to_class

        # Storage for activations and gradients captured by hooks
        self.activations = None
        self.gradients = None

        # ---- Register forward hook to capture feature map activations ----
        self.forward_hook = self.target_layer.register_forward_hook(
            self._forward_hook_fn
        )

        # ---- Register backward hook to capture gradients ----
        self.backward_hook = self.target_layer.register_full_backward_hook(
            self._backward_hook_fn
        )

    def _forward_hook_fn(self, module, input, output):
        """Save the feature map activations during forward pass."""
        self.activations = output.detach()

    def _backward_hook_fn(self, module, grad_input, grad_output):
        """Save the gradients flowing back during backward pass."""
        self.gradients = grad_output[0].detach()

    def generate(self, input_tensor, target_class=None):
        """
        Generate a Grad-CAM heatmap for the given input.

        Args:
            input_tensor: Preprocessed image tensor of shape (1, 3, H, W),
                          already on the correct device.
            target_class: (int or None) Class index to explain.
                          If None, uses the model's top predicted class.

        Returns:
            cam: numpy array of shape (224, 224), normalized to [0, 1]
            predicted_class_idx: int — the predicted (or target) class index
            predicted_class_name: str — human-readable class name
        """
        self.model.eval()

        # ---- Forward pass ----
        input_tensor.requires_grad_(True)
        output = self.model(input_tensor)  # shape: (1, num_classes)
        softmax_scores = torch.nn.functional.softmax(output, dim=1)

        # ---- Determine target class ----
        if target_class is None:
            target_class = output.argmax(dim=1).item()

        predicted_class_idx = target_class
        predicted_class_name = self.class_names.get(predicted_class_idx, "unknown")
        confidence = softmax_scores[0, predicted_class_idx].item() * 100.0

        # ---- Backward pass on the target class score ----
        self.model.zero_grad()
        target_score = output[0, target_class]
        target_score.backward(retain_graph=True)

        # ---- Compute Grad-CAM weights via global average pooling of gradients ----
        # gradients shape: (1, C, H_feat, W_feat)
        if self.gradients is None:
            raise RuntimeError("Gradients were not captured by the backward hook. "
                               "This usually happens if the target layer is frozen or "
                               "not in the gradient path.")
            
        weights = self.gradients.mean(dim=[2, 3], keepdim=True)  # (1, C, 1, 1)

        # ---- Weighted combination of feature maps ----
        # activations shape: (1, C, H_feat, W_feat)
        cam = (weights * self.activations).sum(dim=1, keepdim=True)  # (1, 1, H_feat, W_feat)

        # ---- ReLU to keep only positive contributions ----
        cam = torch.nn.functional.relu(cam)

        # ---- Convert to numpy and resize to input image dimensions ----
        cam = cam.squeeze().cpu().numpy()  # (H_feat, W_feat)
        cam = cv2.resize(cam, (224, 224))

        # ---- Normalize to [0, 1] ----
        cam_min = cam.min()
        cam_max = cam.max()
        if cam_max - cam_min > 1e-8:
            cam = (cam - cam_min) / (cam_max - cam_min)
        else:
            cam = np.zeros_like(cam)

        return cam, predicted_class_idx, predicted_class_name, confidence

    def remove_hooks(self):
        """Remove registered hooks to free memory and avoid side effects."""
        self.forward_hook.remove()
        self.backward_hook.remove()
        self.activations = None
        self.gradients = None


print("✅ GradCAM class defined — supports any CNN with a target convolutional layer")
print("   Usage: cam_obj = GradCAM(model, target_layer)")
print("          cam, pred_idx, pred_name, conf = cam_obj.generate(input_tensor)")
print("          cam_obj.remove_hooks()")
