from typing import Any

from huggingface_hub import hf_hub_download

from src.core.config import Settings
from src.core.logger import get_logger
from src.provider.pest_detector.interface import PestDetectorProvider, PestPrediction


logger = get_logger(__name__)


class Yolo11sPestDetectorProvider(PestDetectorProvider):
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._model: Any | None = None

    def load(self) -> None:
        from ultralytics import YOLO

        logger.info(
            "Loading pest detection model repo_id=%s filename=%s",
            self._settings.pest_model_repo_id,
            self._settings.pest_model_filename,
        )
        model_path = hf_hub_download(
            repo_id=self._settings.pest_model_repo_id,
            filename=self._settings.pest_model_filename,
        )
        self._model = YOLO(model_path)
        logger.info("Pest detection model loaded successfully")

    def predict(self, image_source: Any, top_k: int) -> list[PestPrediction]:
        if self._model is None:
            raise RuntimeError("Pest detection model has not been loaded")

        results = self._model.predict(
            source=image_source,
            imgsz=self._settings.pest_image_size,
            conf=self._settings.pest_confidence_threshold,
            verbose=False,
        )
        if not results:
            return []

        result = results[0]
        predictions = []
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            predictions.append(
                PestPrediction(
                    label=result.names[class_id],
                    confidence=confidence,
                )
            )

        predictions.sort(key=lambda prediction: prediction.confidence, reverse=True)
        return predictions[:top_k]
