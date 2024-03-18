#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A coroutine that executes multiple coroutines at the same time with async.
    Parameter - n: int - The number of times to spawn wait_random function.
    Parameter - max_delay: int - Max delay.
    Return: in ascending order sorted list.
    """

    rand_list = [await wait_random(max_delay) for i in range(n)]
    sorted_list = sorted(rand_list)
    return sorted_list
