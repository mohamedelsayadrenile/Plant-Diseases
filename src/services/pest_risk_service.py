from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


UNKNOWN_RISK_FLAG = "غير معروف"
SEVERE_RISK_FLAG = "شديد الخطورة"


@dataclass(frozen=True)
class PestRiskInfo:
    risk_flag: str
    message: str | None


class PestRiskService:
    def __init__(self, risk_table_path: Path | None = None) -> None:
        self._risk_table_path = risk_table_path or Path(__file__).resolve().parents[2] / "ip102_pest_risk_egypt_ksa.md"
        self._risk_by_label = self._load_risk_table()

    def get_risk_info(self, label: str) -> PestRiskInfo:
        normalized_label = self._normalize_label(label)
        risk_info = self._risk_by_label.get(normalized_label)
        if risk_info is None:
            return PestRiskInfo(risk_flag=UNKNOWN_RISK_FLAG, message=None)
        return risk_info

    def _load_risk_table(self) -> dict[str, PestRiskInfo]:
        if not self._risk_table_path.exists():
            return {}

        risk_by_label: dict[str, PestRiskInfo] = {}
        for line in self._risk_table_path.read_text(encoding="utf-8").splitlines():
            columns = [column.strip() for column in line.strip().strip("|").split("|")]
            if len(columns) != 4 or not columns[0].isdigit():
                continue

            label = columns[1].strip("`")
            risk_flag = columns[2]
            severe_message = columns[3] if risk_flag == SEVERE_RISK_FLAG and columns[3] else None
            risk_by_label[self._normalize_label(label)] = PestRiskInfo(
                risk_flag=risk_flag,
                message=severe_message,
            )

        return risk_by_label

    @staticmethod
    def _normalize_label(label: str) -> str:
        return " ".join(label.strip().lower().split())


@lru_cache
def get_pest_risk_service() -> PestRiskService:
    return PestRiskService()
