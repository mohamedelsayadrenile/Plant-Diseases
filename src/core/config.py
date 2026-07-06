from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="Crop Intelligence API", alias="APP_NAME")
    api_v1_prefix: str = Field(default="/api/v1", alias="API_V1_PREFIX")

    plant_model_repo_id: str = Field(default="eymenslimani/plant-disease-detector", alias="PLANT_MODEL_REPO_ID")
    plant_model_filename: str = Field(default="best_model.pth", alias="PLANT_MODEL_FILENAME")
    plant_model_arch: str = Field(default="tf_efficientnetv2_m.in21k_ft_in1k", alias="PLANT_MODEL_ARCH")
    plant_model_num_classes: int = Field(default=28, alias="PLANT_MODEL_NUM_CLASSES")
    plant_image_size: int = Field(default=256, alias="PLANT_IMAGE_SIZE")

    pest_model_repo_id: str = Field(default="underdogquality/yolo11s-pest-detection", alias="PEST_MODEL_REPO_ID")
    pest_model_filename: str = Field(default="best.pt", alias="PEST_MODEL_FILENAME")
    pest_image_size: int = Field(default=640, alias="PEST_IMAGE_SIZE")
    pest_confidence_threshold: float = Field(default=0.25, alias="PEST_CONFIDENCE_THRESHOLD")

    top_k: int = Field(default=5, alias="TOP_K")
    device: str = Field(default="auto", alias="DEVICE")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[1] / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
