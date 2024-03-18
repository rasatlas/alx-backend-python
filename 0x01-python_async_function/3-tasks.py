#!/usr/bin/env python3
"""A function that returns a asyncio.Task"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that takes an integer and returns a asyncio.Task.
    Parameter - max_delay: int
    Returns - Task
    """

    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)

    return task
