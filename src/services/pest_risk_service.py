from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import pandas as pd


UNKNOWN_RISK_FLAG = "غير معروف"
SEVERE_RISK_FLAG = "شديد الخطورة"


@dataclass(frozen=True)
class PestRiskInfo:
    risk_flag: str
    message: str | None
    recommendation: str | None = None


class PestRiskService:
    def __init__(self, reference_file_path: Path | None = None) -> None:
        self._reference_file_path = reference_file_path or Path(__file__).resolve().parents[2] / "reference.csv"
        self._risk_by_label = self._load_risk_table()

    def get_risk_info(self, label: str) -> PestRiskInfo:
        normalized_label = self._normalize_label(label)
        risk_info = self._risk_by_label.get(normalized_label)
        if risk_info is None:
            return PestRiskInfo(risk_flag=UNKNOWN_RISK_FLAG, message=None)
        return risk_info

    def _load_risk_table(self) -> dict[str, PestRiskInfo]:
        if not self._reference_file_path.exists():
            return {}

        risk_by_label: dict[str, PestRiskInfo] = {}
        df = pd.read_csv(self._reference_file_path)
        for _, row in df.iterrows():
            label = row["class"]
            risk_flag = row["risk level"]
            severe_message = row["message"] if risk_flag == SEVERE_RISK_FLAG and pd.notnull(row["message"]) else None
            recommendation_message = row["recommendation"] if pd.notnull(row["recommendation"]) else None
            risk_by_label[self._normalize_label(label)] = PestRiskInfo(
                risk_flag=risk_flag,
                message=severe_message,
                recommendation=recommendation_message
            )
        return risk_by_label

    @staticmethod
    def _normalize_label(label: str) -> str:
        return " ".join(label.strip().lower().split())


@lru_cache
def get_pest_risk_service() -> PestRiskService:
    return PestRiskService()
