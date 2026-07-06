from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="Plant Disease Classifier API", alias="APP_NAME")
    api_v1_prefix: str = Field(default="/api/v1", alias="API_V1_PREFIX")

    model_repo_id: str = Field(default="eymenslimani/plant-disease-detector", alias="MODEL_REPO_ID")
    model_filename: str = Field(default="best_model.pth", alias="MODEL_FILENAME")
    model_arch: str = Field(default="tf_efficientnetv2_m.in21k_ft_in1k", alias="MODEL_ARCH")
    model_num_classes: int = Field(default=28, alias="MODEL_NUM_CLASSES")

    image_size: int = Field(default=256, alias="IMAGE_SIZE")
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
