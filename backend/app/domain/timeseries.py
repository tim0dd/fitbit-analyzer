from typing import List
from pydantic import BaseModel, Field
from datetime import date, datetime


class BaseTimeSeriesModel(BaseModel):
    timestamp: datetime


class CardioScoreModel(BaseTimeSeriesModel):
    score: float


class SleepScoreModel(BaseTimeSeriesModel):
    score: float


class HeartRateModel(BaseTimeSeriesModel):
    bpm: float


class BreathingRateModel(BaseTimeSeriesModel):
    breaths_per_minute: float


class RestingHeartRateModel(BaseTimeSeriesModel):
    bpm: float


class HRVDeepSleepModel(BaseTimeSeriesModel):
    score: float


class HRVDayModel(BaseTimeSeriesModel):
    score: float


class SkinTemperatureModel(BaseTimeSeriesModel):
    temperature: float


class CaloriesModel(BaseTimeSeriesModel):
    calories: float


class CaloriesBMRModel(BaseTimeSeriesModel):
    calories: float


class MinutesSedentaryModel(BaseTimeSeriesModel):
    minutes: int


class MinutesLightlyActiveModel(BaseTimeSeriesModel):
    minutes: int


class MinutesFairlyActiveModel(BaseTimeSeriesModel):
    minutes: int


class MinutesVeryActiveModel(BaseTimeSeriesModel):
    minutes: int


class StepsModel(BaseTimeSeriesModel):
    steps: int


######### Heart rate json response #########
class HeartRateZone(BaseModel):
    caloriesOut: float
    max: int
    min: int
    minutes: int
    name: str


class HeartRateValue(BaseModel):
    customHeartRateZones: List[HeartRateZone] = []
    heartRateZones: List[HeartRateZone]
    restingHeartRate: int


class ActivitiesHeart(BaseModel):
    dateTime: date
    value: HeartRateValue


class HeartRateIntradayData(BaseModel):
    time: str
    value: int


class ActivitiesHeartIntraday(BaseModel):
    dataset: List[HeartRateIntradayData]
    datasetInterval: int
    datasetType: str


class HeartRateResponse(BaseModel):
    activities_heart: List[ActivitiesHeart]
    activities_heart_intraday: ActivitiesHeartIntraday