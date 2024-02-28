from typing import List, Dict, Union
from fastapi import APIRouter
import pandas as pd

from app.ingest import load_sleep_csv
from typing import List, Dict

from app.util.paths import get_data_path
from typing import List, Dict, Union

router = APIRouter()


@router.get("/overall_score")
def get_overall_score() -> List[Dict[str, Union[int, float]]]:
    return get_sleep_data_column("overall_score")


@router.get("/revitalization_score")
def get_revitalization_score() -> List[Dict[str, Union[int, float]]]:
    return get_sleep_data_column("revitalization_score")


@router.get("/deep_sleep_minutes")
def get_deep_sleep_minutes() -> List[Dict[str, Union[int, float]]]:
    return get_sleep_data_column("deep_sleep_in_minutes")


@router.get("/rhr")
def get_rhr() -> List[Dict[str, Union[int, float]]]:
    return get_sleep_data_column("resting_heart_rate")


@router.get("/restlessness")
def get_restlessness() -> List[Dict[str, Union[int, float]]]:
    return get_sleep_data_column("restlessness")


def get_sleep_data_column(
    column: str, drop_nan_rows=True
) -> List[Dict[str, Union[int, float]]]:
    data = load_sleep_csv.load_sleep_data()
    # check if column exists
    assert column in data.columns, f"Column not found: {column}"
    data = data.reset_index()[["time", column]]
    data = data.rename(columns={column: "value"})
    # convert datetime to UTC seconds ?!
    data["time"] = data["time"].astype("int64") // 10**9
    data.sort_values(by="time", inplace=True)
    if drop_nan_rows:
        data = data.dropna()
    # proper typing to satisfy mypy
    result = [
        {
            "time": int(row["time"]),
            "value": (
                float(row["value"])
                if isinstance(row["value"], float)
                else int(row["value"])
            ),
        }
        for index, row in data.iterrows()
    ]
    return result
