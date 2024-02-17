from typing import Any, Dict, Optional
from app.ingest.fitbit_api.api_base import ApiBase


class GetBreathingRateApiBuilder:
    def __init__(self, api_base: ApiBase):
        self.api_base = api_base
        self.base_url = "https://api.fitbit.com/1/user/-/br/date"
        self.params: Dict[str, Optional[str]] = {}

    def start_date(self, start_date: str) -> "GetBreathingRateApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetBreathingRateApiBuilder":
        self.params["end_date"] = end_date
        return self

    async def exec(self) -> Any:
        start_date = self.params.get("start_date")
        end_date = self.params.get("end_date")
        if not start_date or not end_date:
            raise ValueError("Start date and end date parameters are required.")
        url = f"{self.base_url}/{start_date}/{end_date}.json"
        return await self.api_base._make_get_request(url)
