from src.core.config import Settings
from src.provider.classifier.interface import ClassifierProvider
from src.provider.classifier.providers.plant_disease_detector import PlantDiseaseDetectorProvider


def create_classifier_provider(settings: Settings) -> ClassifierProvider:
    return PlantDiseaseDetectorProvider(settings=settings)
