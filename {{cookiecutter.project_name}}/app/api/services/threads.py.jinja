import asyncio
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


class Thread:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self._pool = ThreadPoolExecutor(max_workers=max_workers)

    async def register(self, func: Callable, *args):
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(self._pool, func, *args)
