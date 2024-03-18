#!/usr/bin/env python3
"""A module that measures the total execution time of a function."""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measures the total execution time for wait_n(n, max_delay).
    Parameters - n: int, max_delay: int
    Return - total_time/n: float
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = (end_time - start_time) / n

    return total_time
