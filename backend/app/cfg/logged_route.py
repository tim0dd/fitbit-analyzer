from fastapi import Response, Request
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse
from fastapi.routing import APIRoute
from typing import Callable
import logging


def log_route(req_body, res_body):
    logging.getLogger(__name__).debug(req_body)
    logging.getLogger(__name__).debug(res_body)


class LoggedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req_body = await request.body()
            response = await original_route_handler(request)

            if isinstance(response, StreamingResponse):
                res_body = b""
                async for item in response.body_iterator:
                    res_body += item if isinstance(item, bytes) else item.encode('utf-8')

                task = BackgroundTask(log_route, req_body, res_body)
                return Response(
                    content=res_body,
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    media_type=response.media_type,
                    background=task,
                )
            else:
                res_body = response.body
                response.background = BackgroundTask(log_route, req_body, res_body)
                return response

        return custom_route_handler
