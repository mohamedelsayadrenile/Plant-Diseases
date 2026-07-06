import asyncio

from src.core.config import Settings
from src.models.schemas.pest_prediction import PestPredictionItem, PestPredictionResponse
from src.provider.pest_detector.interface import PestDetectorProvider
from src.services.image_preprocessing_service import PestImagePreprocessingService
from src.services.pest_risk_service import PestRiskService, get_pest_risk_service


class PestDetectionService:
    def __init__(
        self,
        pest_detector_provider: PestDetectorProvider,
        settings: Settings,
        pest_risk_service: PestRiskService | None = None,
    ) -> None:
        self._pest_detector_provider = pest_detector_provider
        self._settings = settings
        self._image_preprocessor = PestImagePreprocessingService()
        self._pest_risk_service = pest_risk_service or get_pest_risk_service()

    async def predict(self, image_bytes: bytes) -> PestPredictionResponse:
        if not image_bytes:
            raise ValueError("Uploaded image is empty")

        predictions = await asyncio.to_thread(self._predict_sync, image_bytes)
        response_items = []
        for prediction in predictions:
            risk_info = self._pest_risk_service.get_risk_info(prediction.label)
            response_items.append(
                PestPredictionItem(
                    label=prediction.label,
                    confidence=prediction.confidence,
                    risk_flag=risk_info.risk_flag,
                    message=risk_info.message,
                    recommendation=risk_info.recommendation
                )
            )

        return PestPredictionResponse(predictions=response_items)

    def _predict_sync(self, image_bytes: bytes):
        image_source = self._image_preprocessor.decode(image_bytes)
        return self._pest_detector_provider.predict(image_source=image_source, top_k=self._settings.top_k)
