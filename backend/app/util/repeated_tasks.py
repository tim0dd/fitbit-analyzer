from functools import wraps
import aiohttp
import asyncio
import logging
from typing import Callable, Coroutine, Any, List


class RepeatedTaskRegistry:
    def __init__(self):
        self.tasks = {}

    async def start_all(self):
        for task in self.tasks.values():
            await task.start()

    def add(self, name: str, task: "RepeatedTask"):
        self.tasks[name] = task

    def remove(self, name: str, stop=True):
        if name in self.tasks:
            if stop:
                self.tasks[name].stop()
            self.tasks.pop(name)

    def get(self, name: str) -> "RepeatedTask":
        return self.tasks.get(name)

    def stop(self, name: str):
        self.tasks[name].stop()

    def stop_all(self):
        for task in self.tasks.values():
            task.stop()


class RepeatedTask:
    def __init__(
        self, interval_seconds: int, task: Callable[..., Coroutine[Any, Any, Any]]
    ):
        self.interval = interval_seconds
        self.task = task
        self.cancelled = False
        self._task_obj = None

    async def start(self, *args, **kwargs):
        self.cancelled = False
        self._task_obj = asyncio.create_task(self._run(*args, **kwargs))

    async def _run(self, *args, **kwargs):
        while not self.cancelled:
            start_time = asyncio.get_event_loop().time()
            try:
                await self.task(*args, **kwargs)
            except Exception as e:
                logging.error(f"Error in repeated task: {e}", exc_info=True)
            await asyncio.sleep(
                max(0, self.interval - (asyncio.get_event_loop().time() - start_time))
            )

    def stop(self):
        self.cancelled = True
        if self._task_obj and not self._task_obj.done():
            self._task_obj.cancel()