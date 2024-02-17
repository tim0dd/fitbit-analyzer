from enum import Enum
from typing import Any, Dict, Optional
from app.ingest.fitbit_api.api_base import ApiBase

class TempType(Enum):
    SKIN = "skin"
    CORE = "core"

class GetTemperatureApiBuilder:
    def __init__(self, api_base: ApiBase, endpoint: TempType):
        self.api_base = api_base
        self.base_url = f"https://api.fitbit.com/1/user/-/temp/{endpoint.value}"
        self.params: Dict[str, Optional[str]] = {}

    def start_date(self, start_date: str) -> "GetTemperatureApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetTemperatureApiBuilder":
        self.params["end_date"] = end_date
        return self

    async def exec(self) -> Any:
        if not self.params["start_date"] or not self.params["end_date"]:
            raise ValueError("Start date and end date parameters are required.")
        url = f"{self.base_url}/date/{self.params['start_date']}/{self.params['end_date']}.json"
        return await self.api_base._make_get_request(url)
