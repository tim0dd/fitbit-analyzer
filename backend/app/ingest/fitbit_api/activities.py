from enum import Enum
from typing import Any, Dict, Optional
from .api_base import ApiBase


class ActivityResource(Enum):
    ACTIVITY_CALORIES = "activityCalories"
    CALORIES = "calories"
    CALORIES_BMR = "caloriesBMR"
    DISTANCE = "distance"
    ELEVATION = "elevation"
    FLOORS = "floors"
    MINUTES_SEDENTARY = "minutesSedentary"
    MINUTES_LIGHTLY_ACTIVE = "minutesLightlyActive"
    MINUTES_FAIRLY_ACTIVE = "minutesFairlyActive"
    MINUTES_VERY_ACTIVE = "minutesVeryActive"
    STEPS = "steps"


class GetActivitiesApiBuilder:
    def __init__(self, api_base: ApiBase):
        self.api_base = api_base
        self.base_url = "https://api.fitbit.com/1/user/-/activities"
        self.params: Dict[str, Optional[str]] = {}

    def start_date(self, start_date: str) -> "GetActivitiesApiBuilder":
        self.params["start_date"] = start_date
        return self

    def end_date(self, end_date: str) -> "GetActivitiesApiBuilder":
        self.params["end_date"] = end_date
        return self

    def resource_path(
        self, resource_path: ActivityResource
    ) -> "GetActivitiesApiBuilder":
        self.params["resource_path"] = resource_path.value
        return self

    async def exec(self) -> Any:
        if not all(
            key in self.params for key in ["start_date", "end_date", "resource_path"]
        ):
            raise ValueError(
                "Start date, end date, and resource path parameters are required."
            )
        url = f"{self.base_url}/{self.params['resource_path']}/date/{self.params['start_date']}/{self.params['end_date']}.json"
        return await self.api_base._make_get_request(url)
