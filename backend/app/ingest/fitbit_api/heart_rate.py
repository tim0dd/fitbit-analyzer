from typing import Any, Dict, Optional
from .api_base import ApiBase


class GetHeartRateApiBuilder:
    """
    Retrieves the heart rate time series data over a period of time by specifying a date and time period.
    The response will include only the daily summary values.
    """

    def __init__(self, api_base: ApiBase):
        self.api_base = api_base
        self.base_url = "https://api.fitbit.com/1/user/-/activities/heart/date"
        self.params: Dict[str, Optional[str]] = {}

    def date(self, date: str) -> "GetHeartRateApiBuilder":
        self.params["date"] = date
        return self

    def period(self, period: str) -> "GetHeartRateApiBuilder":
        self.params["period"] = period
        return self

    def start_date(self, start_date: str) -> "GetHeartRateApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetHeartRateApiBuilder":
        self.params["end_date"] = end_date
        return self

    async def exec(self) -> Any:
        date = self.params.get("date")
        period = self.params.get("period")
        start_date = self.params.get("start_date")
        end_date = self.params.get("end_date")

        if date and period:
            url = f"{self.base_url}/{date}/{period}.json"
        elif start_date and end_date:
            url = f"{self.base_url}/{start_date}/{end_date}.json"
        else:
            raise ValueError(
                "Either date and period or base date and end date parameters are required."
            )
        return await self.api_base._make_get_request(url)
