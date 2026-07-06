from src.core.config import Settings
from src.provider.pest_detector.interface import PestDetectorProvider
from src.provider.pest_detector.providers.yolo11s_pest_detector import Yolo11sPestDetectorProvider


def create_pest_detector_provider(settings: Settings) -> PestDetectorProvider:
    return Yolo11sPestDetectorProvider(settings=settings)
