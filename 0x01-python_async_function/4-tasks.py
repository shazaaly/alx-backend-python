#!/usr/bin/env python3
"""
     an asynchronous coroutine
     that takes in an integer argument
     (max_delay, with a default value of 10)
    """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values).
in ascending order without using sort() because of concurrency.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
