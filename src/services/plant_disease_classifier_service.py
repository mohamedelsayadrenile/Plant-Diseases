import asyncio

from src.core.config import Settings
from src.models.schemas.prediction import PredictionItem, PredictionResponse
from src.provider.classifier.interface import ClassifierProvider
from src.services.image_preprocessing_service import ImagePreprocessingService


class PlantDiseaseClassifierService:
    def __init__(self, classifier_provider: ClassifierProvider, settings: Settings) -> None:
        self._classifier_provider = classifier_provider
        self._settings = settings
        self._image_preprocessor = ImagePreprocessingService(image_size=settings.image_size)

    async def predict(self, image_bytes: bytes) -> PredictionResponse:
        if not image_bytes:
            raise ValueError("Uploaded image is empty")

        predictions = await asyncio.to_thread(self._predict_sync, image_bytes)
        return PredictionResponse(
            predictions=[
                PredictionItem(label=prediction.label, confidence=prediction.confidence)
                for prediction in predictions
            ]
        )

    def _predict_sync(self, image_bytes: bytes):
        input_tensor = self._image_preprocessor.preprocess(image_bytes)
        return self._classifier_provider.predict(input_tensor=input_tensor, top_k=self._settings.top_k)
