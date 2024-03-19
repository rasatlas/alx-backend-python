#!/usr/bin/env python3
"""A coroutine that yields a random number."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator:
    """A coroutine that yields a random number between 0and 10.
    Parameters: None
    Return: List[float]
    """
    for idx in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
