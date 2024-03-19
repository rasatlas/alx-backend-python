#!/usr/bin/env python3
"""Async comprehension."""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    A coroutine that takes no arguments, collects 10 random numbers using
    an async comprehensing over asyn_generator() and return 10 random numbers.
    Parameters: None
    Return: List[float]
    """
    rand_list = [item async for item in async_generator()]
    return rand_list
