from pathlib import Path

import timm
import torch
from huggingface_hub import hf_hub_download

from src.core.config import Settings
from src.core.logger import get_logger
from src.provider.plant_disease_classifier.interface import (
    PlantDiseaseClassifierProvider,
    PlantDiseasePrediction,
)


logger = get_logger(__name__)


CLASS_NAMES = [
    "Apple_Scab_Leaf",
    "Apple_leaf",
    "Apple_rust_leaf",
    "Bell_pepper_leaf",
    "Bell_pepper_leaf_spot",
    "Blueberry_leaf",
    "Cherry_leaf",
    "Corn_Gray_leaf_spot",
    "Corn_leaf_blight",
    "Corn_rust_leaf",
    "Peach_leaf",
    "Potato_leaf_early_blight",
    "Potato_leaf_late_blight",
    "Raspberry_leaf",
    "Soyabean_leaf",
    "Squash_Powdery_mildew_leaf",
    "Strawberry_leaf",
    "Tomato_Early_blight_leaf",
    "Tomato_Septoria_leaf_spot",
    "Tomato_leaf",
    "Tomato_leaf_bacterial_spot",
    "Tomato_leaf_late_blight",
    "Tomato_leaf_mosaic_virus",
    "Tomato_leaf_yellow_virus",
    "Tomato_mold_leaf",
    "Tomato_two_spotted_spider_mites_leaf",
    "grape_leaf",
    "grape_leaf_black_rot",
]


class PlantDiseaseDetectorProvider(PlantDiseaseClassifierProvider):
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._device = self._resolve_device(settings.device)
        self._model: torch.nn.Module | None = None

    def load(self) -> None:
        logger.info(
            "Loading plant disease model repo_id=%s filename=%s device=%s",
            self._settings.plant_model_repo_id,
            self._settings.plant_model_filename,
            self._device,
        )
        model_path = hf_hub_download(
            repo_id=self._settings.plant_model_repo_id,
            filename=self._settings.plant_model_filename,
        )
        checkpoint = torch.load(
            Path(model_path),
            map_location=self._device,
            weights_only=False,
        )

        model = timm.create_model(
            self._settings.plant_model_arch,
            pretrained=False,
            num_classes=self._settings.plant_model_num_classes,
        )
        state_dict = checkpoint["model_state_dict"] if isinstance(checkpoint, dict) else checkpoint
        model.load_state_dict(state_dict)
        model.to(self._device)
        model.eval()

        self._model = model
        logger.info("Plant disease model loaded successfully")

    def predict(self, input_tensor: torch.Tensor, top_k: int) -> list[PlantDiseasePrediction]:
        if self._model is None:
            raise RuntimeError("Plant disease model has not been loaded")

        top_k = min(top_k, len(CLASS_NAMES))
        input_tensor = input_tensor.to(self._device)

        with torch.inference_mode():
            logits = self._model(input_tensor)
            probabilities = torch.softmax(logits, dim=1)
            confidence_values, class_indices = torch.topk(probabilities, k=top_k, dim=1)

        return [
            PlantDiseasePrediction(
                label=CLASS_NAMES[class_index],
                confidence=float(confidence),
            )
            for confidence, class_index in zip(
                confidence_values[0].detach().cpu().tolist(),
                class_indices[0].detach().cpu().tolist(),
                strict=True,
            )
        ]

    @staticmethod
    def _resolve_device(configured_device: str) -> torch.device:
        if configured_device == "auto":
            return torch.device("cuda" if torch.cuda.is_available() else "cpu")
        return torch.device(configured_device)
