#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer argument."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """An asynchronous coroutine that takes in an integer argument
    with a default value of 10 that waits for a random delay between
    0 and max_delay, including float values, seconds and eventually
    returns it.

    Parameter: max_delay: integer
    Return: random_val: float
    """

    rand_val = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
