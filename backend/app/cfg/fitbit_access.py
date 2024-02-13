import json
import logging
import os

from app.util.paths import get_root_path

FITBIT_ACCESS_TOKEN_ENV_VAR = "FITBIT_ACCESS_TOKEN"


def try_find_fitbit_access_token() -> bool:
    token_from_env = get_fitbit_access_token_from_env()
    if token_from_env is not None:
        logging.info(
            f"Fitbit access token found in environment variable {FITBIT_ACCESS_TOKEN_ENV_VAR}. Using it to make requests to the Fitbit API."
        )
        return True

    json_token_path = f"{get_root_path()}/credentials/fitbit.json"
    logging.info(
        f"Fitbit access token not found in environment variable {FITBIT_ACCESS_TOKEN_ENV_VAR}. Trying to load access token from the value corresponding to key 'fitbit_access_token' in {json_token_path}"
    )
    # try to read it from the json file
    json_not_found_msg = f"Fitbit access token not found in '{json_token_path}'. Backend will not be able to make requests to the Fitbit API."
    if os.path.exists(json_token_path):
        with open(json_token_path, "r") as file:
            token_from_json = json.load(file).get("fitbit_access_token")
            if token_from_json is not None:
                print("Fitbit access token successfully loaded from json file.")
                os.environ["FITBIT_ACCESS_TOKEN"] = token_from_json
                return True
            else:
                logging.warning(json_not_found_msg)
    else:
        logging.warning(json_not_found_msg)
    return False


def get_fitbit_access_token_from_env() -> str | None:
    token = os.environ.get(FITBIT_ACCESS_TOKEN_ENV_VAR)
    if token is None or token != "":
        return None
    return token
