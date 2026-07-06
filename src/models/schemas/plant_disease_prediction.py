from pydantic import BaseModel, Field


class PlantDiseasePredictionItem(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)


class PlantDiseasePredictionResponse(BaseModel):
    predictions: list[PlantDiseasePredictionItem]
