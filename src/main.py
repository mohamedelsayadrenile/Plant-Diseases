from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.v1.endpoints.prediction import router as prediction_router
from src.core.config import settings
from src.core.logger import configure_logging, get_logger
from src.provider.classifier.factory import create_classifier_provider
from src.services.plant_disease_classifier_service import PlantDiseaseClassifierService


configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    classifier_provider = create_classifier_provider(settings=settings)
    classifier_provider.load()
    app.state.classifier_service = PlantDiseaseClassifierService(
        classifier_provider=classifier_provider,
        settings=settings,
    )
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(prediction_router, prefix=settings.api_v1_prefix)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
