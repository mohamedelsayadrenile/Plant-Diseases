from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1.endpoints.pest_prediction import router as pest_prediction_router
from src.api.v1.endpoints.plant_disease_prediction import router as plant_disease_prediction_router
from src.core.config import settings
from src.core.logger import configure_logging, get_logger
from src.provider.pest_detector.factory import create_pest_detector_provider
from src.provider.plant_disease_classifier.factory import create_plant_disease_classifier_provider
from src.services.pest_detection_service import PestDetectionService
from src.services.plant_disease_classifier_service import PlantDiseaseClassifierService


configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    plant_disease_classifier_provider = create_plant_disease_classifier_provider(settings=settings)
    plant_disease_classifier_provider.load()
    app.state.plant_disease_classifier_service = PlantDiseaseClassifierService(
        classifier_provider=plant_disease_classifier_provider,
        settings=settings,
    )

    pest_detector_provider = create_pest_detector_provider(settings=settings)
    pest_detector_provider.load()
    app.state.pest_detection_service = PestDetectionService(
        pest_detector_provider=pest_detector_provider,
        settings=settings,
    )
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(plant_disease_prediction_router, prefix=settings.api_v1_prefix)
app.include_router(pest_prediction_router, prefix=settings.api_v1_prefix)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
