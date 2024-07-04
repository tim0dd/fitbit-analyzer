db = db.getSiblingDB('db');

timeseriesCollections = [
    "cardio_score",
    "sleep_score",
    "heart_rate",
    "hrv_deep_sleep",
    "hrv_day",
    "breathing_rate",
    "skin_temperature",
    "calories",
    "calories_bmr",
    "minutes_sedentary",
    "minutes_lightly_active",
    "minutes_fairly_active",
    "minutes_very_active",
    "steps",
]

collections = [
    "fitbit_sync_awareness",
]

for (var i = 0; i < timeseriesCollections.length; i++) {
    db.createCollection(timeseriesCollections[i], {
        timeseries: {
            timeField: 'timestamp',
            granularity: 'seconds'
        },
    });
}

for (var i = 0; i < collections.length; i++) {
    db.createCollection(collections[i]);
}