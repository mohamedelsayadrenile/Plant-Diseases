import asyncio

from src.core.config import Settings
from src.models.schemas.pest_prediction import PestPredictionItem, PestPredictionResponse
from src.models.schemas.plant_disease_prediction import (
    PlantPredictionItem,
    PlantDiseasePredictionResponse,
)
from src.provider.plant_disease_classifier.interface import PlantDiseaseClassifierProvider
from src.services.image_preprocessing_service import ImagePreprocessingService
from src.services.plant_risk_service import PestRiskService, get_pest_risk_service


class PlantDiseaseClassifierService:
    def __init__(self, classifier_provider: PlantDiseaseClassifierProvider, settings: Settings) -> None:
        self._classifier_provider = classifier_provider
        self._settings = settings
        self._image_preprocessor = ImagePreprocessingService(image_size=settings.plant_image_size)
        self._plant_risk_service = get_pest_risk_service()

    async def predict(self, image_bytes: bytes) -> PlantDiseasePredictionResponse:
        if not image_bytes:
            raise ValueError("Uploaded image is empty")

        predictions = await asyncio.to_thread(self._predict_sync, image_bytes)
        response_items = []
        for prediction in predictions:
            risk_info = self._plant_risk_service.get_risk_info(prediction.label)
            response_items.append(
                PlantPredictionItem(
                    label=prediction.label,
                    confidence=prediction.confidence,
                    risk_flag=risk_info.risk_flag,
                    message=risk_info.message,
                    recommendation=risk_info.recommendation
                )
            )

        return PlantDiseasePredictionResponse(predictions=response_items)

    def _predict_sync(self, image_bytes: bytes):
        input_tensor = self._image_preprocessor.preprocess(image_bytes)
        return self._classifier_provider.predict(input_tensor=input_tensor, top_k=self._settings.top_k)
