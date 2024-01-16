#!/usr/bin/env python3

"""
 a measure_runtime coroutine that will execute
 async_comprehension four times in parallel
 using asyncio.gather.

measure_runtime should measure the total r
untime and return it.

"""


import random, asyncio
from time import time
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
 a coroutine that will execute async_comprehension
 four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.

 """
    time_before = time()
    res = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    time_after = time()

    return time_after - time_before


