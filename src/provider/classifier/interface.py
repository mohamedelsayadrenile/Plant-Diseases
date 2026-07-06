from abc import ABC, abstractmethod
from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class ClassificationPrediction:
    label: str
    confidence: float


class ClassifierProvider(ABC):
    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict(self, input_tensor: torch.Tensor, top_k: int) -> list[ClassificationPrediction]:
        raise NotImplementedError
