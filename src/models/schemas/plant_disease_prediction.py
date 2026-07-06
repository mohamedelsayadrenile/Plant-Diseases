from pydantic import BaseModel, Field


class PlantPredictionItem(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    risk_flag: str
    message: str | None = None
    recommendation: str | None = None


class PlantDiseasePredictionResponse(BaseModel):
    predictions: list[PlantPredictionItem]
