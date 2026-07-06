from src.core.config import Settings
from src.provider.plant_disease_classifier.interface import PlantDiseaseClassifierProvider
from src.provider.plant_disease_classifier.providers.plant_disease_detector import PlantDiseaseDetectorProvider


def create_plant_disease_classifier_provider(settings: Settings) -> PlantDiseaseClassifierProvider:
    return PlantDiseaseDetectorProvider(settings=settings)
