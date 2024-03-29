#!/usr/bin/env python3
""" Module defining make_multiplier function. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier
    """
    def func(num: float):
        return num * multiplier
    return func
