from pydantic import BaseModel
from datetime import datetime


class FitbitSyncAwareness(BaseModel):
    series_name: str
    last_updated: datetime
    next_fetch_start_date: datetime
    next_fetch_end_date: datetime
