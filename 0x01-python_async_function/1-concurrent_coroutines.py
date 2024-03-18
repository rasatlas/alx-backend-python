#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async."""


async def wait_n(n: int, max_delay: int) -> list:
    """Doc String
    Parameters:
    Return:
    """
    rand_list = [await __import__('0-basic_async_syntax').
                 wait_random(max_delay) for i in range(n)]
    return rand_list
