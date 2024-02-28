from typing import Any, Dict, Optional
from .api_base import ApiBase


class GetCardioFitnessApiBuilder:
    def __init__(self, api_base: ApiBase):
        self.api_base = api_base
        self.base_url = "https://api.fitbit.com/1/user/-/cardioscore/date"
        self.params: Dict[str, Optional[str]] = {}


    def start_date(self, start_date: str) -> "GetCardioFitnessApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetCardioFitnessApiBuilder":
        self.params["end_date"] = end_date
        return self

    async def exec(self) -> Any:
        if not self.params.get("start_date") or not self.params.get("end_date"):
            raise ValueError("Start date and end date parameters are required.")
        url = (
            f"{self.base_url}/{self.params['start_date']}/{self.params['end_date']}.json"
        )
        return await self.api_base._make_get_request(url)