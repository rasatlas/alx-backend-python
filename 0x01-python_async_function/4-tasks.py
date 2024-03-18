#!/usr/bin/env python3
"""A function that alters wait_n() into a new function."""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """A function that alters wait_n() function into task_wait_n().
    Parameters - n: int, max_delay: int
    Returns: List[float]
    """
    ls = [task_wait_random(max_delay) for i in range(n)]
    stop = [await task for task in asyncio.as_completed(ls)]
    return stop
