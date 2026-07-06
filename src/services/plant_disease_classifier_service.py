import asyncio

from src.core.config import Settings
from src.models.schemas.plant_disease_prediction import (
    PlantDiseasePredictionItem,
    PlantDiseasePredictionResponse,
)
from src.provider.plant_disease_classifier.interface import PlantDiseaseClassifierProvider
from src.services.image_preprocessing_service import ImagePreprocessingService


class PlantDiseaseClassifierService:
    def __init__(self, classifier_provider: PlantDiseaseClassifierProvider, settings: Settings) -> None:
        self._classifier_provider = classifier_provider
        self._settings = settings
        self._image_preprocessor = ImagePreprocessingService(image_size=settings.plant_image_size)

    async def predict(self, image_bytes: bytes) -> PlantDiseasePredictionResponse:
        if not image_bytes:
            raise ValueError("Uploaded image is empty")

        predictions = await asyncio.to_thread(self._predict_sync, image_bytes)
        return PlantDiseasePredictionResponse(
            predictions=[
                PlantDiseasePredictionItem(label=prediction.label, confidence=prediction.confidence)
                for prediction in predictions
            ]
        )

    def _predict_sync(self, image_bytes: bytes):
        input_tensor = self._image_preprocessor.preprocess(image_bytes)
        return self._classifier_provider.predict(input_tensor=input_tensor, top_k=self._settings.top_k)
