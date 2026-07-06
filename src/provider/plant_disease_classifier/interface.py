from abc import ABC, abstractmethod
from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class PlantDiseasePrediction:
    label: str
    confidence: float


class PlantDiseaseClassifierProvider(ABC):
    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict(self, input_tensor: torch.Tensor, top_k: int) -> list[PlantDiseasePrediction]:
        raise NotImplementedError
