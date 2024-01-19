#!/usr/bin/env python3
"""
     an asynchronous coroutine
     that takes in an integer argument
     (max_delay, with a default value of 10)
    """

wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List
import asyncio

async def wait_n(n, max_delay) -> List[float]:
    """_summary_
    """
    sorted_tasks = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = asyncio.as_completed(tasks)
    for task in completed:
        result = await task
        sorted_tasks.append(result)
    return sorted_tasks