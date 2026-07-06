from pydantic import BaseModel, Field


class PredictionItem(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)


class PredictionResponse(BaseModel):
    predictions: list[PredictionItem]
