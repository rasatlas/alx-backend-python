#!/usr/bin/env python3
"""Calculating run time for four parallel comprehenisons."""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A coroutine that weill execute async_comprehension() four times in
    parallel using asyncio.gather.
    Parameters: None
    Return: Total run time: float
    """
    time_start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    time_end = time.perf_counter()

    return time_end - time_start
