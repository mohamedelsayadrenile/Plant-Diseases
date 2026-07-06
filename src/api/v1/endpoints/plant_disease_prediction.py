from fastapi import APIRouter, HTTPException, Request, UploadFile, status

from src.core.logger import get_logger
from src.models.schemas.plant_disease_prediction import PlantDiseasePredictionResponse
from src.services.image_preprocessing_service import InvalidImageError
from src.services.plant_disease_classifier_service import PlantDiseaseClassifierService


logger = get_logger(__name__)
router = APIRouter(prefix="/plant-diseases/predictions", tags=["plant diseases"])


def get_plant_disease_classifier_service(request: Request) -> PlantDiseaseClassifierService:
    return request.app.state.plant_disease_classifier_service


@router.post("", response_model=PlantDiseasePredictionResponse)
async def predict_plant_disease(request: Request, file: UploadFile) -> PlantDiseasePredictionResponse:
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Uploaded file must be an image",
        )

    image_bytes = await file.read()
    classifier_service = get_plant_disease_classifier_service(request)

    try:
        return await classifier_service.predict(image_bytes=image_bytes)
    except InvalidImageError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except Exception:
        logger.exception("Plant disease prediction failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Plant disease prediction failed",
        )
