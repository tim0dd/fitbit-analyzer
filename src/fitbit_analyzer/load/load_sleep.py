import pandas as pd

def load_sleep_data(path: str) -> pd.DataFrame:
    """
    Load fitbit sleep score data from an exported CSV file. 

    The CSV file contains the following columns:
    - sleep_log_entry_id: Unique identifier for each sleep log entry.
    - timestamp: Timestamp for the sleep data entry (Unix format).
    - overall_score: Overall sleep quality score (between 0 and 100).
    - composition_score: Score based on the sleep composition (between 0 and 100).
    - revitalization_score: Score based on how revitalizing the sleep was (between 0 and 100).
    - duration_score: Score based on the duration of sleep (empty values for me, probably depending on tracker model).
    - deep_sleep_in_minutes: Amount of time spent in deep sleep, in minutes.
    - resting_heart_rate: Resting heart rate during sleep.
    - restlessness: Measure of restlessness during sleep (seemingly a value between 0 and 1).

    As of January 2024, this dataset is provided in a single CSV file.

    :param path: Path to the sleep score data.
    :return: DataFrame containing the sleep score data.
    """
    
    data = pd.read_csv(path, sep=',')
    data = data.drop(columns=['sleep_log_entry_id']) # don't need this column
    if data['duration_score'].isnull().all():
        data = data.drop(columns=['duration_score'])
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.rename(columns={'timestamp': 'time'})
    data = data.set_index('time')
    data['restlessness'] = data['restlessness'] * 100
    # print headers
    print('Headers:' + str(data.columns))
    return data
