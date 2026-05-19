DISEASE_INFO = {

    # ==================== APPLE ====================
    "Apple___Apple_scab": {
        "disease_name": "Apple Scab",
        "pathogen": "Venturia inaequalis",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can cause significant defoliation and fruit loss if untreated."
        },
        "description": (
            "Apple scab causes olive-green to black velvety lesions on leaves and fruit. "
            "Severe infections lead to premature leaf drop and unmarketable fruit."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy fallen infected leaves immediately.",
                "Prune affected branches to improve air circulation.",
                "Avoid overhead irrigation to reduce leaf wetness duration."
            ],
            "chemical_treatment": [
                "Captan 50 WP — Apply 2.5 g/L as a protective spray every 7–10 days during wet periods.",
                "Myclobutanil (Rally) — Apply 0.3 mL/L as a curative and protective fungicide.",
                "Mancozeb 75 WP — Apply 2.5 g/L at green-tip stage; repeat at 7-day intervals."
            ],
            "cultural_practices": [
                "Sanitation — Rake and destroy fallen leaves in autumn to reduce overwintering inoculum.",
                "Resistant varieties — Consider planting Liberty, Enterprise, or GoldRush.",
                "Proper spacing — Ensure adequate tree spacing to promote air circulation."
            ]
        }
    },

    "Apple___Black_rot": {
        "disease_name": "Black Rot",
        "pathogen": "Botryosphaeria obtusa",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can destroy fruit and weaken trees over successive seasons."
        },
        "description": (
            "Black rot causes brown, concentric-ringed lesions on fruit and 'frogeye' leaf spots. "
            "Cankers on branches serve as a persistent source of infection."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove mummified fruit and cankers from the tree immediately.",
                "Prune dead or infected wood at least 15 cm below visible canker margins.",
                "Do not compost infected material — dispose in sealed bags or burn."
            ],
            "chemical_treatment": [
                "Captan 50 WP — Apply 2.5 g/L every 7–10 days from bloom through harvest.",
                "Thiophanate-methyl (Topsin-M) — Apply 1.0 g/L during early bloom for canker control.",
                "Copper fungicide (Kocide 3000) — Apply at green-tip for broad-spectrum protection."
            ],
            "cultural_practices": [
                "Sanitation — Remove all mummified fruit and prune dead wood annually during dormancy.",
                "Fire blight management — Control fire blight as dead wood provides entry points for black rot.",
                "Proper pruning — Maintain open canopy to reduce humidity and improve spray coverage."
            ]
        }
    },

    "Apple___Cedar_apple_rust": {
        "disease_name": "Cedar Apple Rust",
        "pathogen": "Gymnosporangium juniperi-virginianae",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Causes leaf spots and fruit deformation; rarely kills trees but reduces yield."
        },
        "description": (
            "Cedar apple rust produces bright orange-yellow spots on apple leaves and fruit. "
            "The fungus requires both apple and juniper/cedar hosts to complete its lifecycle."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove galls from nearby juniper/cedar trees before spring sporulation.",
                "Pick off heavily infected leaves to slow disease spread.",
                "Avoid planting apple trees within 300 meters of juniper/cedar hosts."
            ],
            "chemical_treatment": [
                "Myclobutanil (Rally) — Apply 0.3 mL/L starting at pink bud stage; repeat every 7–10 days.",
                "Mancozeb 75 WP — Apply 2.5 g/L as protective spray beginning at green-tip.",
                "Triadimefon (Bayleton) — Apply 0.15 g/L for systemic control during bloom."
            ],
            "cultural_practices": [
                "Host separation — Remove or avoid planting junipers/cedars near apple orchards.",
                "Resistant varieties — Consider planting Liberty, Redfree, or Freedom apple cultivars.",
                "Monitoring — Scout for galls on juniper hosts in late winter for early management."
            ]
        }
    },

    "Apple___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The apple leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for early signs of disease."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Consider preventive fungicide schedule if disease pressure is historically high in your region."
            ],
            "cultural_practices": [
                "Maintain proper nutrition — Apply balanced fertilizer based on soil test results.",
                "Ensure adequate watering — Deep, infrequent irrigation is preferred over shallow, frequent watering.",
                "Sanitation — Continue removing fallen debris and pruning dead wood annually."
            ]
        }
    },

    # ==================== BLUEBERRY ====================
    "Blueberry___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The blueberry leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for pests and diseases."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive fungicide applications may be considered during prolonged wet seasons."
            ],
            "cultural_practices": [
                "Maintain soil acidity — Keep soil pH between 4.5 and 5.5 for optimal health.",
                "Mulching — Apply pine bark or wood chip mulch to retain moisture and suppress weeds.",
                "Pruning — Remove old, unproductive canes annually to encourage vigorous growth."
            ]
        }
    },

    # ==================== CHERRY ====================
    "Cherry_(including_sour)___Powdery_mildew": {
        "disease_name": "Powdery Mildew",
        "pathogen": "Podosphaera clandestina",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Reduces photosynthesis and fruit quality; can stunt young trees."
        },
        "description": (
            "Powdery mildew appears as white, powdery fungal growth on leaves, shoots, and fruit. "
            "Young leaves curl and become distorted; fruit may crack or develop poor color."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy heavily infected shoots and leaves.",
                "Improve air circulation by thinning dense canopy areas.",
                "Avoid excessive nitrogen fertilization, which promotes susceptible succulent growth."
            ],
            "chemical_treatment": [
                "Myclobutanil (Rally) — Apply 0.3 mL/L at first sign of infection; repeat every 10–14 days.",
                "Sulfur-based fungicide — Apply 3–5 g/L as a preventive spray; avoid use above 30°C.",
                "Trifloxystrobin (Flint) — Apply 0.15 g/L alternating with DMI fungicides to prevent resistance."
            ],
            "cultural_practices": [
                "Proper spacing — Ensure adequate tree spacing for good air movement.",
                "Resistant varieties — Select powdery mildew-tolerant rootstocks and cultivars.",
                "Water management — Use drip irrigation; avoid wetting foliage in the evening."
            ]
        }
    },

    "Cherry_(including_sour)___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The cherry leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Monitor regularly, especially during humid conditions."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive sprays at bloom may be beneficial in disease-prone areas."
            ],
            "cultural_practices": [
                "Maintain balanced nutrition — Avoid excess nitrogen which promotes disease-susceptible growth.",
                "Proper pruning — Open-center pruning improves air circulation and sunlight penetration.",
                "Sanitation — Remove fallen leaves and pruning debris to reduce inoculum sources."
            ]
        }
    },

    # ==================== CORN (MAIZE) ====================
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "disease_name": "Gray Leaf Spot",
        "pathogen": "Cercospora zeae-maydis",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can cause severe yield loss (up to 50%) under favorable humid conditions."
        },
        "description": (
            "Gray leaf spot produces rectangular, grayish-tan lesions that run parallel to leaf veins. "
            "Severe infections cause premature leaf death, reducing photosynthesis and grain fill."
        ),
        "treatment": {
            "immediate_actions": [
                "Scout fields regularly from V6 stage onward for early lesion detection.",
                "Remove lower infected leaves if feasible in small-scale operations.",
                "Avoid overhead irrigation to reduce prolonged leaf wetness."
            ],
            "chemical_treatment": [
                "Azoxystrobin (Quadris) — Apply 0.6 mL/L at first sign of disease; repeat at 14-day intervals.",
                "Pyraclostrobin + Metconazole (Headline AMP) — Apply at VT/R1 stage for optimal protection.",
                "Propiconazole (Tilt) — Apply 0.5 mL/L as a foliar spray when disease threshold is met."
            ],
            "cultural_practices": [
                "Crop rotation — Rotate with non-host crops (soybean, small grains) for 1–2 seasons.",
                "Tillage — Incorporate crop residue by plowing to reduce overwintering fungal spores.",
                "Resistant hybrids — Plant hybrids with high Gray Leaf Spot resistance ratings."
            ]
        }
    },

    "Corn_(maize)___Common_rust_": {
        "disease_name": "Common Rust",
        "pathogen": "Puccinia sorghi",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 3,
            "label": "Low-Moderate",
            "description": "Usually causes minor yield loss; severe outbreaks are uncommon in resistant hybrids."
        },
        "description": (
            "Common rust produces small, circular to elongated, reddish-brown pustules on both leaf surfaces. "
            "Heavy infections can reduce photosynthetic area and grain fill in susceptible hybrids."
        ),
        "treatment": {
            "immediate_actions": [
                "Monitor fields from V8 stage, especially during cool (16–23°C), humid weather.",
                "Assess rust severity before tasseling to decide on fungicide application.",
                "Remove and destroy volunteer corn plants that harbor rust spores."
            ],
            "chemical_treatment": [
                "Mancozeb 75 WP — Apply 2.5 g/L as a protective spray at early pustule formation.",
                "Azoxystrobin (Quadris) — Apply 0.6 mL/L before tasseling if pustule density is high.",
                "Propiconazole (Tilt) — Apply 0.5 mL/L when >50% of plants show pustules before tasseling."
            ],
            "cultural_practices": [
                "Resistant hybrids — Plant hybrids with strong common rust resistance genes (e.g., Rp genes).",
                "Planting date — Avoid late planting which exposes corn to higher spore loads.",
                "Field monitoring — Regular scouting enables timely fungicide decisions."
            ]
        }
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "disease_name": "Northern Leaf Blight",
        "pathogen": "Exserohilum turcicum",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can cause 30–50% yield loss when upper leaves are severely affected before grain fill."
        },
        "description": (
            "Northern Leaf Blight produces large (2–15 cm), cigar-shaped, grayish-green to tan lesions on leaves. "
            "Lesions often start on lower leaves and progress upward; severe cases lead to premature drying."
        ),
        "treatment": {
            "immediate_actions": [
                "Scout lower leaves from V8 stage for characteristic cigar-shaped lesions.",
                "Assess disease severity at VT stage to determine fungicide application needs.",
                "Remove heavily infected crop debris post-harvest to reduce inoculum."
            ],
            "chemical_treatment": [
                "Azoxystrobin + Propiconazole (Quilt) — Apply 1.0 mL/L at first sign near VT/R1 stage.",
                "Picoxystrobin (Aproach) — Apply 0.5 mL/L as a preventive spray if weather favors disease.",
                "Mancozeb 75 WP — Apply 2.5 g/L as an early-season protectant in rotation with systemic fungicides."
            ],
            "cultural_practices": [
                "Crop rotation — Rotate with soybean or small grains for at least 1 year.",
                "Residue management — Till or chop corn stubble to accelerate decomposition of infected residue.",
                "Resistant hybrids — Select hybrids with Ht1, Ht2, or Ht3 resistance genes."
            ]
        }
    },

    "Corn_(maize)___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The corn leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue routine scouting at weekly intervals throughout the growing season."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Consider a preventive fungicide at VT/R1 in fields with a history of foliar diseases."
            ],
            "cultural_practices": [
                "Balanced fertilization — Apply nitrogen based on soil tests and yield goals.",
                "Crop rotation — Rotate with legumes to break disease cycles and improve soil health.",
                "Weed management — Control weeds that compete for nutrients and harbor pest populations."
            ]
        }
    },

    # ==================== GRAPE ====================
    "Grape___Black_rot": {
        "disease_name": "Black Rot",
        "pathogen": "Guignardia bidwellii",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 6,
            "label": "High",
            "description": "Can destroy up to 80% of the crop if left untreated in warm, humid climates."
        },
        "description": (
            "Black rot causes circular, tan leaf spots with dark borders and black pycnidia. "
            "Infected berries shrivel into hard, black mummies that serve as the primary inoculum source."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove all mummified berries from vines and the ground immediately.",
                "Prune out infected canes and destroy them — do not compost.",
                "Improve canopy airflow by removing excess shoots and positioning shoots vertically."
            ],
            "chemical_treatment": [
                "Myclobutanil (Rally) — Apply 0.3 mL/L from shoot emergence to veraison at 10–14 day intervals.",
                "Mancozeb 75 WP — Apply 2.5 g/L as a protectant from early bloom; discontinue 66 days before harvest.",
                "Captan 50 WP — Apply 2.5 g/L alternating with systemic fungicides for resistance management."
            ],
            "cultural_practices": [
                "Sanitation — Remove all mummified fruit and infected wood during dormant-season pruning.",
                "Canopy management — Open canopy through leaf pulling and shoot positioning to improve air circulation.",
                "Resistant varieties — Consider cultivars like Concord, Norton, or Chambourcin in disease-prone areas."
            ]
        }
    },

    "Grape___Esca_(Black_Measles)": {
        "disease_name": "Esca (Black Measles)",
        "pathogen": "Complex — Phaeomoniella chlamydospora, Phaeoacremonium spp., Fomitiporia spp.",
        "pathogen_type": "Fungal Complex",
        "severity": {
            "level": 7,
            "label": "Very High",
            "description": "Chronic, often fatal trunk disease; can cause sudden vine death (apoplexy)."
        },
        "description": (
            "Esca causes tiger-stripe patterns on leaves and dark spotting on berries (black measles). "
            "Internal wood shows dark streaking and soft rot. Acute form causes sudden, complete vine collapse."
        ),
        "treatment": {
            "immediate_actions": [
                "Mark symptomatic vines immediately for monitoring and possible removal.",
                "Cut back dead cordons/trunks to healthy tissue; disinfect tools between cuts.",
                "Remove severely infected vines entirely and destroy them to prevent spread."
            ],
            "chemical_treatment": [
                "Sodium arsenite — Historically used but now banned in most countries; no fully effective chemical exists.",
                "Fosetyl-Aluminum (Aliette) — Apply as a trunk injection (experimental) to slow fungal progression.",
                "Trichoderma-based biocontrol (Trichodex) — Apply to pruning wounds to prevent new infections."
            ],
            "cultural_practices": [
                "Pruning wound protection — Apply wound sealant or biocontrol agents immediately after pruning.",
                "Late pruning — Prune during late dormancy when wounds heal faster, reducing infection windows.",
                "Trunk renewal — Retrain new trunks from suckers to replace infected wood over time."
            ]
        }
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "disease_name": "Leaf Blight (Isariopsis Leaf Spot)",
        "pathogen": "Pseudocercospora vitis (syn. Isariopsis clavispora)",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Causes premature defoliation; moderate yield impact if not controlled."
        },
        "description": (
            "Leaf blight produces angular, dark-brown necrotic spots with yellow halos on grape leaves. "
            "Severe cases lead to premature defoliation, weakening the vine and reducing fruit quality."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy severely infected leaves to reduce spore load.",
                "Avoid overhead watering — use drip irrigation instead.",
                "Improve vine spacing and canopy management for better air circulation."
            ],
            "chemical_treatment": [
                "Mancozeb 75 WP — Apply 2.5 g/L at first sign of spots; repeat every 7–10 days.",
                "Copper oxychloride — Apply 3 g/L as a protective spray during wet weather.",
                "Carbendazim 50 WP — Apply 1 g/L as a systemic fungicide at 14-day intervals."
            ],
            "cultural_practices": [
                "Sanitation — Remove fallen leaves and debris from the vineyard floor after harvest.",
                "Canopy management — Thin shoots and pull leaves around fruit zone for airflow.",
                "Balanced fertilization — Avoid excess nitrogen; ensure adequate potassium for leaf health."
            ]
        }
    },

    "Grape___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The grape leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular scouting, especially during bloom and veraison."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive fungicide programs are recommended in humid regions."
            ],
            "cultural_practices": [
                "Canopy management — Maintain an open canopy through regular shoot thinning and leaf pulling.",
                "Cover crops — Use appropriate cover crops to improve soil health and reduce erosion.",
                "Balanced nutrition — Apply fertilizer based on tissue and soil analysis."
            ]
        }
    },

    # ==================== ORANGE ====================
    "Orange___Haunglongbing_(Citrus_greening)": {
        "disease_name": "Huanglongbing (Citrus Greening)",
        "pathogen": "Candidatus Liberibacter asiaticus",
        "pathogen_type": "Bacterium",
        "severity": {
            "level": 7,
            "label": "Very High",
            "description": "Incurable, fatal disease; most devastating citrus disease worldwide."
        },
        "description": (
            "HLB causes asymmetric blotchy mottling of leaves, lopsided bitter fruit, and eventual tree decline. "
            "The bacterium is transmitted by the Asian citrus psyllid (Diaphorina citri) and is currently incurable."
        ),
        "treatment": {
            "immediate_actions": [
                "Report suspected HLB to local agricultural authorities immediately.",
                "Remove and destroy confirmed infected trees to prevent spread.",
                "Control Asian citrus psyllid populations aggressively in and around the grove."
            ],
            "chemical_treatment": [
                "Imidacloprid (Admire Pro) — Soil drench at 0.5 mL/L for systemic psyllid control.",
                "Spinetaram (Delegate) — Foliar spray at 0.35 mL/L targeting psyllid nymphs and adults.",
                "Oxytetracycline trunk injection — Used under special permits for HLB management in some regions."
            ],
            "cultural_practices": [
                "Psyllid management — Implement area-wide coordinated psyllid control programs.",
                "Certified nursery stock — Plant only HLB-free trees from certified, screened nurseries.",
                "Nutritional therapy — Enhanced foliar nutrition (micronutrients) may prolong productivity of infected trees."
            ]
        }
    },

    # ==================== PEACH ====================
    "Peach___Bacterial_spot": {
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas arboricola pv. pruni",
        "pathogen_type": "Bacterium",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Causes significant leaf loss and fruit blemishes; difficult to control."
        },
        "description": (
            "Bacterial spot causes angular, water-soaked lesions on leaves that turn purple-brown, "
            "often with shot-hole appearance. Fruit develop shallow, sunken, cracked spots."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove heavily infected leaves and fruit to reduce bacterial inoculum.",
                "Avoid overhead irrigation and working among wet plants.",
                "Ensure proper tree nutrition, especially adequate zinc and nitrogen."
            ],
            "chemical_treatment": [
                "Copper hydroxide (Kocide 3000) — Apply 1.5 g/L at leaf fall and early spring; avoid phytotoxicity.",
                "Oxytetracycline (Mycoshield) — Apply 1.5 g/L at bloom and petal fall; repeat at 7-day intervals.",
                "Copper + Mancozeb tank mix — Apply during dormant season for combined bacterial and fungal control."
            ],
            "cultural_practices": [
                "Resistant varieties — Plant resistant cultivars such as Clayton, Contender, or Harrow Beauty.",
                "Site selection — Choose well-drained sites with good air circulation and full sun.",
                "Windbreaks — Establish windbreaks to reduce wind-driven rain that spreads bacteria."
            ]
        }
    },

    "Peach___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The peach leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for bacterial spot and brown rot."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Dormant copper spray is recommended annually as a preventive measure."
            ],
            "cultural_practices": [
                "Pruning — Open-center pruning promotes air circulation and sunlight penetration.",
                "Thinning — Thin fruit to proper spacing (15–20 cm) for larger, healthier fruit.",
                "Soil health — Maintain organic matter with compost and cover crops."
            ]
        }
    },

    # ==================== PEPPER (BELL) ====================
    "Pepper,_bell___Bacterial_spot": {
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas campestris pv. vesicatoria",
        "pathogen_type": "Bacterium",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can cause severe defoliation and fruit damage under warm, wet conditions."
        },
        "description": (
            "Bacterial spot causes small, dark, water-soaked lesions on leaves, stems, and fruit. "
            "Leaf lesions may coalesce, causing extensive yellowing and defoliation."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove infected plant parts immediately — do not compost; dispose in sealed bags.",
                "Avoid overhead watering; water at base level only to reduce spread.",
                "Do not handle plants when foliage is wet to prevent bacterial transmission."
            ],
            "chemical_treatment": [
                "Copper hydroxide (Kocide 3000) — Apply 1.5 g/L every 5–7 days during wet weather.",
                "Acibenzolar-S-methyl (Actigard) — Apply 0.07 g/L as a plant defense activator; alternate with copper.",
                "Copper + Mancozeb tank mix — Apply 1.5 g/L + 2.5 g/L to improve efficacy and reduce copper resistance."
            ],
            "cultural_practices": [
                "Crop rotation — Avoid planting peppers or tomatoes in the same field for 2–3 years.",
                "Certified seed — Use pathogen-free, hot-water-treated seed to prevent seed-borne infection.",
                "Resistant varieties — Consider varieties with Bs2 or Bs3 resistance genes."
            ]
        }
    },

    "Pepper,_bell___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The bell pepper leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for bacterial spot and other foliar diseases."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive copper sprays may be applied during extended wet periods."
            ],
            "cultural_practices": [
                "Proper spacing — Space plants 45–60 cm apart for adequate air circulation.",
                "Mulching — Apply straw or plastic mulch to reduce soil splash onto foliage.",
                "Balanced fertilization — Ensure adequate calcium to prevent blossom end rot."
            ]
        }
    },

    # ==================== POTATO ====================
    "Potato___Early_blight": {
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can reduce yield by 20–50% through premature defoliation."
        },
        "description": (
            "Early blight causes dark brown to black, concentric-ringed ('target-like') lesions on older leaves. "
            "The disease progresses from lower to upper canopy and can also affect tubers."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove infected leaves immediately — do not compost; dispose in sealed bags.",
                "Avoid overhead watering; water at base level only to reduce spread.",
                "Ensure proper plant spacing for air circulation."
            ],
            "chemical_treatment": [
                "Mancozeb 75 WP — Apply 2.5 g/L every 7–10 days as a protectant starting at tuber initiation.",
                "Chlorothalonil — Apply as a broad-spectrum fungicide; alternate with other chemistries to prevent resistance.",
                "Azoxystrobin (Amistar) — Apply 0.5 mL/L for systemic protection; rotate with contact fungicides."
            ],
            "cultural_practices": [
                "Crop rotation — Avoid potato/tomato family for 2–3 seasons in the same field.",
                "Resistant varieties — Consider Celebrity, Mountain Supreme, or Kennebec for next planting.",
                "Adequate nutrition — Ensure sufficient nitrogen and phosphorus; stressed plants are more susceptible."
            ]
        }
    },

    "Potato___Late_blight": {
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans",
        "pathogen_type": "Oomycete",
        "severity": {
            "level": 7,
            "label": "Very High",
            "description": "Highly destructive; can destroy an entire field within days under favorable conditions."
        },
        "description": (
            "Late blight causes large, water-soaked, dark green to brown lesions with white sporulation on leaf undersides. "
            "The disease spreads explosively in cool, wet weather and can also cause severe tuber rot."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy all infected plants immediately — burn or bag them; do NOT compost.",
                "Apply fungicide within 24 hours of first detection.",
                "Alert neighboring farms — late blight spores travel long distances via wind."
            ],
            "chemical_treatment": [
                "Metalaxyl + Mancozeb (Ridomil Gold MZ) — Apply 2.5 g/L immediately upon detection; repeat every 7 days.",
                "Chlorothalonil (Bravo) — Apply 2.0 g/L as a protectant in a 5–7 day spray schedule.",
                "Cymoxanil + Mancozeb (Curzate M) — Apply 2.5 g/L with curative and protectant action."
            ],
            "cultural_practices": [
                "Destroy cull piles — Eliminate all volunteer potatoes and cull piles that harbor the pathogen.",
                "Resistant varieties — Plant varieties like Defender, Jacqueline Lee, or Sarpo Mira.",
                "Harvest management — Kill vines 2–3 weeks before harvest to reduce tuber infection."
            ]
        }
    },

    "Potato___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The potato leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue scouting for early blight and late blight, especially during wet periods."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive fungicide applications are recommended in late blight-prone regions."
            ],
            "cultural_practices": [
                "Certified seed — Always use certified, disease-free seed potatoes.",
                "Hilling — Maintain adequate soil cover over tubers to prevent greening and disease entry.",
                "Crop rotation — Rotate with non-solanaceous crops for at least 2 years."
            ]
        }
    },

    # ==================== RASPBERRY ====================
    "Raspberry___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The raspberry leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for common raspberry diseases and pests."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Dormant lime-sulfur spray may be applied as a preventive measure."
            ],
            "cultural_practices": [
                "Cane management — Remove spent floricanes after harvest to improve airflow.",
                "Trellising — Support canes with a trellis to keep fruit off the ground.",
                "Weed control — Maintain a clean row base to reduce humidity and disease pressure."
            ]
        }
    },

    # ==================== SOYBEAN ====================
    "Soybean___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The soybean leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue routine scouting for sudden death syndrome and soybean rust."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Seed treatment fungicides are recommended for early-season protection."
            ],
            "cultural_practices": [
                "Inoculation — Use appropriate Bradyrhizobium inoculant for optimal nitrogen fixation.",
                "Row spacing — Adjust row spacing for canopy closure to suppress weeds naturally.",
                "Crop rotation — Rotate with corn or small grains to break disease and pest cycles."
            ]
        }
    },

    # ==================== SQUASH ====================
    "Squash___Powdery_mildew": {
        "disease_name": "Powdery Mildew",
        "pathogen": "Podosphaera xanthii / Erysiphe cichoracearum",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Reduces photosynthesis and yield; fruits may ripen prematurely with poor quality."
        },
        "description": (
            "Powdery mildew appears as white, talcum-like powdery coating on upper and lower leaf surfaces. "
            "Severely infected leaves yellow, brown, and die prematurely, reducing fruit size and quality."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy severely infected leaves to slow the spread.",
                "Increase plant spacing to improve air circulation around foliage.",
                "Avoid excessive nitrogen fertilization which promotes dense, susceptible growth."
            ],
            "chemical_treatment": [
                "Potassium bicarbonate (MilStop) — Apply 3 g/L as a contact fungicide every 7–10 days.",
                "Myclobutanil (Rally) — Apply 0.3 mL/L at first sign of disease; alternate with protectants.",
                "Sulfur-based fungicide — Apply 3–5 g/L as a preventive spray; avoid application above 30°C."
            ],
            "cultural_practices": [
                "Resistant varieties — Plant powdery mildew-resistant squash varieties (check seed catalogs for PM resistance).",
                "Proper spacing — Space plants adequately (90–120 cm) to maximize airflow.",
                "Drip irrigation — Avoid overhead watering; although PM doesn't require free water, overall plant health improves."
            ]
        }
    },

    # ==================== STRAWBERRY ====================
    "Strawberry___Leaf_scorch": {
        "disease_name": "Leaf Scorch",
        "pathogen": "Diplocarpon earlianum",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Causes defoliation and weakens plants; reduces yield in the following season."
        },
        "description": (
            "Leaf scorch causes irregular, dark purple blotches on leaves that coalesce, giving a scorched appearance. "
            "Unlike leaf spot, it lacks a defined center; severely infected plants may lose most leaves by fall."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy severely infected leaves and plant debris.",
                "Avoid overhead irrigation; water at the base of plants early in the morning.",
                "Improve air circulation by removing runners and thinning plant density."
            ],
            "chemical_treatment": [
                "Captan 50 WP — Apply 2.5 g/L starting at bloom; repeat every 7–10 days.",
                "Myclobutanil (Rally) — Apply 0.3 mL/L as a systemic fungicide at 14-day intervals.",
                "Copper fungicide — Apply 2 g/L post-harvest (after renovation) for season-long protection."
            ],
            "cultural_practices": [
                "Renovation — Mow and renovate strawberry beds immediately after harvest to remove infected foliage.",
                "Resistant varieties — Consider planting Allstar, Earliglow, or Jewel which show good resistance.",
                "Site selection — Plant in well-drained soil with full sun and good air movement."
            ]
        }
    },

    "Strawberry___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The strawberry leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular monitoring for leaf spot, leaf scorch, and gray mold."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive captan sprays during bloom can protect against fruit rots."
            ],
            "cultural_practices": [
                "Mulching — Apply straw mulch to keep fruit clean and reduce soil-borne disease.",
                "Runner management — Remove excess runners to maintain optimal plant spacing.",
                "Renovation — Renovate beds annually after harvest for continued vigor."
            ]
        }
    },

    # ==================== TOMATO ====================
    "Tomato___Bacterial_spot": {
        "disease_name": "Bacterial Spot",
        "pathogen": "Xanthomonas vesicatoria / X. euvesicatoria / X. gardneri / X. perforans",
        "pathogen_type": "Bacterium",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Causes severe defoliation, fruit lesions, and significant yield loss in warm, wet conditions."
        },
        "description": (
            "Bacterial spot causes small, dark, water-soaked lesions on leaves, stems, and fruit. "
            "Leaf spots may have yellow halos; fruit develops raised, scab-like blemishes."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy infected plant material — do not compost.",
                "Avoid working with plants when foliage is wet to prevent bacterial spread.",
                "Reduce overhead irrigation; switch to drip irrigation immediately."
            ],
            "chemical_treatment": [
                "Copper hydroxide (Kocide 3000) — Apply 1.5 g/L every 5–7 days; begin at transplanting.",
                "Copper + Mancozeb tank mix — Apply to improve efficacy and reduce copper-resistant bacterial populations.",
                "Acibenzolar-S-methyl (Actigard) — Apply 0.07 g/L to activate plant systemic resistance."
            ],
            "cultural_practices": [
                "Crop rotation — Rotate away from tomato/pepper for at least 2 years.",
                "Certified seed — Use hot-water-treated (50°C for 25 minutes) or certified disease-free seed.",
                "Resistant varieties — Select varieties with resistance to prevalent Xanthomonas races."
            ]
        }
    },

    "Tomato___Early_blight": {
        "disease_name": "Early Blight",
        "pathogen": "Alternaria solani",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Causes progressive defoliation and can reduce yield by 30–50%."
        },
        "description": (
            "Early blight produces dark brown, concentric-ringed 'target-spot' lesions on lower leaves first. "
            "Lesions progress upward; severe defoliation exposes fruit to sunscald."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove infected lower leaves immediately — do not compost; dispose in sealed bags.",
                "Avoid overhead watering; water at base level only to reduce spread.",
                "Stake or cage plants to keep foliage off the ground."
            ],
            "chemical_treatment": [
                "Mancozeb 75 WP — Apply 2.5 g/L every 7–10 days starting at first flower.",
                "Chlorothalonil (Bravo) — Broad-spectrum fungicide; alternate with systemic products to prevent resistance.",
                "Azoxystrobin (Amistar) — Apply 0.5 mL/L for systemic control; limit to 2 consecutive applications."
            ],
            "cultural_practices": [
                "Crop rotation — Avoid tomato/potato family for 2–3 seasons.",
                "Resistant varieties — Consider Celebrity, Mountain Supreme, or Defiant PHR for next planting.",
                "Mulching — Apply organic or plastic mulch to prevent soil splashing onto lower leaves."
            ]
        }
    },

    "Tomato___Late_blight": {
        "disease_name": "Late Blight",
        "pathogen": "Phytophthora infestans",
        "pathogen_type": "Oomycete",
        "severity": {
            "level": 7,
            "label": "Very High",
            "description": "Extremely destructive; can kill plants within days and spread rapidly across fields."
        },
        "description": (
            "Late blight causes large, irregular, water-soaked, dark green to brown lesions on leaves and stems. "
            "White fuzzy sporulation appears on leaf undersides in humid conditions; fruit develop firm, brown rot."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy ALL infected plants immediately — bag or burn; never compost.",
                "Apply fungicide within 24 hours of first symptom detection.",
                "Notify nearby growers — spores spread via wind for many kilometers."
            ],
            "chemical_treatment": [
                "Metalaxyl + Mancozeb (Ridomil Gold MZ) — Apply 2.5 g/L upon detection; repeat every 5–7 days.",
                "Chlorothalonil (Bravo) — Apply 2.0 g/L as a protectant on a strict 5-day schedule during outbreaks.",
                "Mandipropamid (Revus) — Apply 0.6 mL/L for translaminar protection; excellent rain fastness."
            ],
            "cultural_practices": [
                "Sanitation — Remove all plant debris at end of season; do not leave infected material in the field.",
                "Resistant varieties — Plant varieties like Iron Lady, Defiant PHR, Mountain Magic, or Legend.",
                "Avoid overhead irrigation — Use drip irrigation only; minimize leaf wetness duration."
            ]
        }
    },

    "Tomato___Leaf_Mold": {
        "disease_name": "Leaf Mold",
        "pathogen": "Passalora fulva (syn. Cladosporium fulvum)",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Primarily a greenhouse problem; can cause significant defoliation and yield loss indoors."
        },
        "description": (
            "Leaf mold causes pale green to yellow spots on upper leaf surfaces with olive-green to brown velvety "
            "sporulation on the undersides. It thrives in high humidity (>85%) and moderate temperatures."
        ),
        "treatment": {
            "immediate_actions": [
                "Increase ventilation immediately in greenhouses — open vents and use fans.",
                "Remove and destroy heavily infected leaves to reduce spore load.",
                "Reduce humidity below 85% by increasing air circulation and reducing irrigation frequency."
            ],
            "chemical_treatment": [
                "Chlorothalonil (Bravo) — Apply 2.0 g/L every 7–10 days as a protectant.",
                "Mancozeb 75 WP — Apply 2.5 g/L alternating with systemic fungicides.",
                "Copper fungicide — Apply 2 g/L in organic production systems; repeat every 7 days."
            ],
            "cultural_practices": [
                "Greenhouse management — Maintain relative humidity below 85%; use dehumidifiers if necessary.",
                "Resistant varieties — Many greenhouse varieties carry Cf resistance genes (Cf-2, Cf-4, Cf-5, Cf-9).",
                "Plant spacing — Increase spacing and prune lower leaves for improved airflow."
            ]
        }
    },

    "Tomato___Septoria_leaf_spot": {
        "disease_name": "Septoria Leaf Spot",
        "pathogen": "Septoria lycopersici",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Causes extensive defoliation starting from lower canopy; yield loss can be severe."
        },
        "description": (
            "Septoria leaf spot produces numerous small, circular spots with dark borders and grayish-white centers "
            "containing tiny black pycnidia. Starts on lower leaves and spreads rapidly in wet conditions."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove infected lower leaves immediately — bag and dispose; do not compost.",
                "Avoid overhead watering; irrigate at the base of plants in the morning.",
                "Stake or trellis plants to improve air circulation and reduce soil splash."
            ],
            "chemical_treatment": [
                "Chlorothalonil (Bravo) — Apply 2.0 g/L every 7 days starting at first flower or first symptoms.",
                "Mancozeb 75 WP — Apply 2.5 g/L alternating with chlorothalonil for resistance management.",
                "Copper fungicide (Kocide 3000) — Apply 1.5 g/L as an organic-approved option; repeat weekly."
            ],
            "cultural_practices": [
                "Crop rotation — Avoid planting tomatoes in the same area for at least 2 years.",
                "Mulching — Apply organic or plastic mulch to prevent rain-splashed soil from reaching lower leaves.",
                "Sanitation — Remove and destroy all tomato debris at end of season; clean tools between uses."
            ]
        }
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "disease_name": "Spider Mite Infestation (Two-Spotted Spider Mite)",
        "pathogen": "Tetranychus urticae",
        "pathogen_type": "Arachnid (Pest — not a disease pathogen)",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Can cause rapid leaf stippling, bronzing, defoliation, and yield loss in hot, dry conditions."
        },
        "description": (
            "Two-spotted spider mites feed on leaf undersides, causing fine stippling and yellowing. "
            "Heavy infestations produce visible webbing; leaves turn bronze and dry out, leading to plant decline."
        ),
        "treatment": {
            "immediate_actions": [
                "Spray infested plants with a strong jet of water to physically dislodge mites.",
                "Isolate heavily infested plants to prevent spread to healthy plants.",
                "Increase humidity around plants — mites thrive in hot, dry conditions."
            ],
            "chemical_treatment": [
                "Abamectin (Agri-Mek) — Apply 0.3 mL/L targeting leaf undersides; repeat after 7 days.",
                "Spiromesifen (Oberon) — Apply 0.5 mL/L as a growth regulator miticide; excellent translaminar activity.",
                "Neem oil (Azadirachtin) — Apply 3 mL/L as an organic option; repeat every 5–7 days."
            ],
            "cultural_practices": [
                "Biological control — Release predatory mites (Phytoseiulus persimilis) for sustainable mite management.",
                "Avoid broad-spectrum insecticides — These kill natural predators and cause mite resurgence.",
                "Weed management — Remove weed hosts (clover, pigweed) around fields that harbor mite populations."
            ]
        }
    },

    "Tomato___Target_Spot": {
        "disease_name": "Target Spot",
        "pathogen": "Corynespora cassiicola",
        "pathogen_type": "Fungus",
        "severity": {
            "level": 4,
            "label": "Moderate",
            "description": "Can cause significant defoliation and fruit lesions in warm, humid environments."
        },
        "description": (
            "Target spot produces brown, concentric-ringed lesions on leaves, stems, and fruit. "
            "Lesions start small but can expand rapidly and merge, causing large areas of necrosis."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove infected lower leaves and destroy them to slow the spread.",
                "Improve air circulation by pruning suckers and staking plants.",
                "Avoid overhead irrigation; use drip irrigation to keep foliage dry."
            ],
            "chemical_treatment": [
                "Chlorothalonil (Bravo) — Apply 2.0 g/L every 7–10 days as a protectant starting at early fruiting.",
                "Azoxystrobin (Amistar) — Apply 0.5 mL/L for systemic control; alternate with contact fungicides.",
                "Difenoconazole (Score) — Apply 0.5 mL/L for curative and protective action."
            ],
            "cultural_practices": [
                "Crop rotation — Rotate with non-host crops for at least 2 years.",
                "Sanitation — Remove all plant debris at the end of the season; C. cassiicola survives in crop residue.",
                "Proper spacing — Ensure adequate spacing (60–90 cm) for airflow and spray penetration."
            ]
        }
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "pathogen": "Tomato yellow leaf curl virus (TYLCV)",
        "pathogen_type": "Virus (Begomovirus, family Geminiviridae)",
        "severity": {
            "level": 7,
            "label": "Very High",
            "description": "Can cause 100% yield loss in susceptible varieties; no cure once infected."
        },
        "description": (
            "TYLCV causes severe upward curling and yellowing of leaf margins, stunted growth, and flower drop. "
            "Plants infected early produce little to no fruit. Transmitted by the whitefly Bemisia tabaci."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy all infected plants immediately — bag and dispose; do not compost.",
                "Control whitefly populations aggressively on and around infected plants.",
                "Install yellow sticky traps to monitor and reduce whitefly populations."
            ],
            "chemical_treatment": [
                "Imidacloprid (Confidor) — Soil drench at 0.5 mL/L for systemic whitefly control at transplanting.",
                "Pyriproxyfen (Admiral) — Apply 0.5 mL/L as an insect growth regulator targeting whitefly nymphs.",
                "Cyantraniliprole (Cyazypyr) — Apply 0.75 mL/L for dual action against whiteflies and lepidopteran pests."
            ],
            "cultural_practices": [
                "Resistant varieties — Plant TYLCV-resistant hybrids (e.g., Ty-1, Ty-2, Ty-3 gene carriers).",
                "Physical barriers — Use UV-reflective mulch and fine-mesh insect netting (50-mesh) over transplants.",
                "Crop-free period — Enforce a tomato-free period in the region to break the whitefly-virus cycle."
            ]
        }
    },

    "Tomato___Tomato_mosaic_virus": {
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "pathogen": "Tomato mosaic virus (ToMV)",
        "pathogen_type": "Virus (Tobamovirus, family Virgaviridae)",
        "severity": {
            "level": 5,
            "label": "Moderate-High",
            "description": "Reduces fruit quality and yield; extremely contagious through mechanical contact."
        },
        "description": (
            "ToMV causes mottled light and dark green mosaic patterns on leaves, leaf curling, and stunted growth. "
            "Fruit may show internal browning (brownwall) and uneven ripening. The virus is extremely stable and transmissible."
        ),
        "treatment": {
            "immediate_actions": [
                "Remove and destroy infected plants immediately — the virus is highly contagious.",
                "Wash hands with soap/milk and disinfect tools with 10% bleach between handling plants.",
                "Do not smoke or use tobacco products near tomato plants — tobacco can carry ToMV."
            ],
            "chemical_treatment": [
                "No chemical treatment can cure viral infections.",
                "Milk spray (10% skim milk solution) — Apply as a foliar spray to reduce mechanical transmission.",
                "Imidacloprid (Confidor) — Apply 0.5 mL/L as soil drench if aphid vectors are contributing to spread."
            ],
            "cultural_practices": [
                "Resistant varieties — Plant varieties carrying the Tm-2² resistance gene (most modern hybrids have this).",
                "Seed treatment — Use certified virus-free seed; treat seed with 10% trisodium phosphate for 15 minutes.",
                "Sanitation — Disinfect all tools, stakes, and greenhouse surfaces with 10% bleach or commercial virucide."
            ]
        }
    },

    "Tomato___healthy": {
        "disease_name": "Healthy",
        "pathogen": "N/A",
        "pathogen_type": "N/A",
        "severity": {
            "level": 0,
            "label": "No Disease",
            "description": "The plant appears healthy with no visible signs of disease."
        },
        "description": "No disease detected. The tomato leaf appears healthy and normal.",
        "treatment": {
            "immediate_actions": [
                "No immediate action required.",
                "Continue regular scouting for early blight, late blight, and viral symptoms."
            ],
            "chemical_treatment": [
                "No chemical treatment necessary.",
                "Preventive fungicide programs starting at first flower are recommended in disease-prone areas."
            ],
            "cultural_practices": [
                "Staking/Caging — Support plants to improve air circulation and reduce soil splash.",
                "Mulching — Apply mulch to maintain soil moisture and prevent rain-splashed pathogens.",
                "Crop rotation — Avoid planting tomatoes or other Solanaceae in the same location for 3 years."
            ]
        }
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_disease_info(class_name: str) -> dict:
    """
    Returns the full disease information dictionary for a given PlantVillage class name.

    Parameters
    ----------
    class_name : str
        One of the 38 PlantVillage class names (e.g. 'Tomato___Early_blight').

    Returns
    -------
    dict or str
        Disease information dictionary or an error message if class not found.
    """
    if class_name in DISEASE_INFO:
        return DISEASE_INFO[class_name]
    return {"error": f"Class '{class_name}' not found. Please use one of the 38 PlantVillage class names."}


def get_severity_badge(class_name: str) -> str:
    """
    Returns a formatted severity badge string for UI display.

    Example output: '🔴 Moderate-High (5/7)'
    """
    info = DISEASE_INFO.get(class_name)
    if not info:
        return "❓ Unknown class"

    level = info["severity"]["level"]
    label = info["severity"]["label"]

    badge_map = {
        0: "🟢",   # No Disease
        1: "🟢",   # Very Low
        2: "🟡",   # Low
        3: "🟡",   # Low-Moderate
        4: "🟠",   # Moderate
        5: "🔴",   # Moderate-High
        6: "🔴",   # High
        7: "⛔",   # Very High
    }
    emoji = badge_map.get(level, "❓")
    return f"{emoji} {label} ({level}/7)"


def format_treatment_card(class_name: str) -> str:
    """
    Returns a formatted treatment card string for console/UI display,
    matching the style in the uploaded image.
    """
    info = DISEASE_INFO.get(class_name)
    if not info:
        return "Class not found."

    t = info["treatment"]
    lines = []
    lines.append(f"{'='*55}")
    lines.append(f"  🌿 {info['disease_name']}  |  {get_severity_badge(class_name)}")
    lines.append(f"  Pathogen: {info['pathogen']} ({info['pathogen_type']})")
    lines.append(f"{'='*55}")
    lines.append(f"\n  ── IMMEDIATE ACTION ──")
    for action in t["immediate_actions"]:
        lines.append(f"  🟫 {action}")
    lines.append(f"\n  ── CHEMICAL TREATMENT ──")
    for chem in t["chemical_treatment"]:
        lines.append(f"  🧪 {chem}")
    lines.append(f"\n  ── CULTURAL PRACTICES ──")
    for practice in t["cultural_practices"]:
        lines.append(f"  🌱 {practice}")
    lines.append(f"\n{'='*55}")
    return "\n".join(lines)


# ============================================================
# DEMO / TEST
# ============================================================
if __name__ == "__main__":
    # Print all 38 class names
    print(f"Total classes in DISEASE_INFO: {len(DISEASE_INFO)}\n")
    for idx, key in enumerate(DISEASE_INFO.keys(), 1):
        severity = get_severity_badge(key)
        print(f"  {idx:>2}. {key:<55} {severity}")

    # Demo: Print a full treatment card
    print("\n")
    print(format_treatment_card("Potato___Early_blight"))
    print(format_treatment_card("Tomato___Late_blight"))
    print(format_treatment_card("Grape___Esca_(Black_Measles)"))