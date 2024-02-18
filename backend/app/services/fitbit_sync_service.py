from app.ingest.fitbit_api.api_base import ApiBase
from app.util.repeated_tasks import RepeatedTask, RepeatedTaskRegistry
from app.ingest.fitbit_api.sleep import GetSleepApiBuilder
from app.ingest.fitbit_api.breathing_rate import GetBreathingRateApiBuilder
from app.ingest.fitbit_api.cardio_fitness import GetCardioFitnessApiBuilder
from app.ingest.fitbit_api.heart_rate import GetHeartRateApiBuilder
from app.ingest.fitbit_api.hrv import GetHrvApiBuilder
from app.ingest.fitbit_api.temperature import GetTemperatureApiBuilder
from app.cfg import fitbit_access
from app.util.paths import get_data_path
import json


class FitbitSyncService:
    def __init__(self):
        access_token = fitbit_access.get_fitbit_access_token_from_env()
        self.api_base = ApiBase(access_token)
        self.repeated_task_registry = RepeatedTaskRegistry()
        interval_seconds = 10
        self.repeated_task_registry.add(
            "fitbit_sync", RepeatedTask(interval_seconds, self.fitbit_sync)
        )

    async def start_sync(self):
        await self.repeated_task_registry.start_all()

    def stop_sync(self):
        self.repeated_task_registry.stop_all()

    async def fitbit_sync(self):
        get_breathing_rate_req = (
            GetBreathingRateApiBuilder(self.api_base)
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )
        get_cardio_fitness_req = (
            GetCardioFitnessApiBuilder(self.api_base)
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )
        get_heart_rate_req = (
            GetHeartRateApiBuilder(self.api_base).date("2023-01-01").period("1d")
        )
        get_hrv_req = (
            GetHrvApiBuilder(self.api_base)
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )

        get_sleep_req = (
            GetSleepApiBuilder(self.api_base)  # TODO: look into params
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )
        get_skin_temperature_req = (
            GetTemperatureApiBuilder(self.api_base, "skin")
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )
        get_core_temperature_req = (
            GetTemperatureApiBuilder(self.api_base, "core")
            .start_date("2023-01-01")
            .end_date("2023-01-02")
        )

        breathing_rate_response = await get_breathing_rate_req.exec()
        print(breathing_rate_response)
        dump_to_json("breathing_rate", breathing_rate_response)
        cardio_fitness_response = await get_cardio_fitness_req.exec()
        print(cardio_fitness_response)
        dump_to_json("cardio_fitness", cardio_fitness_response)
        heart_rate_response = await get_heart_rate_req.exec()
        print(heart_rate_response)
        dump_to_json("heart_rate", heart_rate_response)
        hrv_response = await get_hrv_req.exec()
        print(hrv_response)
        dump_to_json("hrv", hrv_response)
        sleep_response = await get_sleep_req.exec()
        print(sleep_response)
        dump_to_json("sleep", sleep_response)
        skin_temperature_response = await get_skin_temperature_req.exec()
        print(skin_temperature_response)
        dump_to_json("skin_temperature", skin_temperature_response)
        core_temperature_response = await get_core_temperature_req.exec()
        print(core_temperature_response)
        dump_to_json("core_temperature", core_temperature_response)


def dump_to_json(name: str, data: dict):
    path = get_data_path()
    with open(f"{path}/{name}.json", "w") as f:
        json.dump(data, f, indent=4)
