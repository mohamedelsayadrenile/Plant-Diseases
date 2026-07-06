from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PestPrediction:
    label: str
    confidence: float


class PestDetectorProvider(ABC):
    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict(self, image_source: Any, top_k: int) -> list[PestPrediction]:
        raise NotImplementedError
