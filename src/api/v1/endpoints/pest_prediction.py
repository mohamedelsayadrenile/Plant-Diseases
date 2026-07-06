from fastapi import APIRouter, HTTPException, Request, UploadFile, status

from src.core.logger import get_logger
from src.models.schemas.pest_prediction import PestPredictionResponse
from src.services.image_preprocessing_service import InvalidImageError
from src.services.pest_detection_service import PestDetectionService


logger = get_logger(__name__)
router = APIRouter(prefix="/pests/predictions", tags=["pests"])


def get_pest_detection_service(request: Request) -> PestDetectionService:
    return request.app.state.pest_detection_service


@router.post("", response_model=PestPredictionResponse)
async def predict_pests(request: Request, file: UploadFile) -> PestPredictionResponse:
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Uploaded file must be an image",
        )

    image_bytes = await file.read()
    pest_detection_service = get_pest_detection_service(request)

    try:
        return await pest_detection_service.predict(image_bytes=image_bytes)
    except InvalidImageError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except Exception:
        logger.exception("Pest prediction failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Pest prediction failed",
        )
