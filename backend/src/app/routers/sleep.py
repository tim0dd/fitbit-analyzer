from typing import List, Dict, Union
from fastapi import APIRouter

from app.ingest import load_sleep
from typing import List, Dict, Any

router = APIRouter()

@router.get("/data_series")
def get_data_series() -> List[Dict[str, Union[int, float]]]:
    data = load_sleep.load_sleep_data()
    data = data.reset_index()[["time", "overall_score"]]
    data = data.rename(columns={"overall_score": "value"})
    # convert datetime to UTC seconds ?!
    data["time"] = data["time"].astype('int64') // 10**9
    data.sort_values(by="time", inplace=True)
    return data.to_dict(orient="records")
