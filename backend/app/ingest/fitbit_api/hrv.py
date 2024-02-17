from typing import Any, Dict, Optional
from app.ingest.fitbit_api.api_base import ApiBase


class GetHrvApiBuilder:
    def __init__(self, api_base: ApiBase):
        self.api_base = api_base
        self.base_url = "https://api.fitbit.com/1/user/-/hrv/date"
        self.params: Dict[str, Optional[str]] = {}

    def date(self, date: str) -> "GetHrvApiBuilder":
        self.params["date"] = date
        return self

    def start_date(self, start_date: str) -> "GetHrvApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetHrvApiBuilder":
        self.params["end_date"] = end_date
        return self

    async def exec(self) -> Any:
        if "date" in self.params:
            url = f"{self.base_url}/{self.params['date']}.json"
        elif "start_date" in self.params and "end_date" in self.params:
            url = f"{self.base_url}/{self.params['start_date']}/{self.params['end_date']}.json"
        else:
            raise ValueError("Insufficient parameters for request.")

        return await self.api_base._make_get_request(url)
