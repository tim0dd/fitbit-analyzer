import logging
import aiohttp
from aiohttp import ClientResponseError
from typing import Any, Optional


class ApiBase:
    def __init__(self, access_token: str):
        self.logger = logging.getLogger(__name__)
        self.access_token = access_token
        self.api_client = aiohttp.ClientSession()
        self.api_client.headers.update({"Authorization": f"Bearer {access_token}"})

    async def _make_get_request(self, url: str, params: Optional[dict] = None) -> Any:
        try:
            async with self.api_client.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except ClientResponseError as e:
            self.logger.error(
                f"Client error during GET request: {e}. Error details: {e.__dict__}"
            )
        except Exception as e:
            self.logger.error(f"Unexpected error during GET request: {e}")
