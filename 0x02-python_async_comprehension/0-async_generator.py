#!/usr/bin/env python3
"""A coroutine that yields a random number."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that yields a random number between 0and 10.
    Parameters: None
    Return: List[float]
    """
    for idx in range(10):
        # suspend and sleep a moment
        await asyncio.sleep(1)
        # yield a value to the caller
        yield random.uniform(0, 10)
