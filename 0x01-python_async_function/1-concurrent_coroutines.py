#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async."""
import asyncio


async def wait_n(n: int, max_delay: int) -> list:
    """
    A coroutine that executes multiple coroutines at the same time with async.
    Parameter - n: int - The number of times to spawn wait_random function.
    Parameter - max_delay: int - Max delay.
    Return: list
    """

    async_module = __import__('0-basic_async_syntax')
    rand_list = [await async_module.wait_random(max_delay) for i in range(n)]
    sorted_list = sorted(rand_list)
    return sorted_list
