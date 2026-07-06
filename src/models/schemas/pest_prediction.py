from pydantic import BaseModel, Field


class PestPredictionItem(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    risk_flag: str
    message: str | None = None
    recommendation: str | None = None


class PestPredictionResponse(BaseModel):
    predictions: list[PestPredictionItem]
