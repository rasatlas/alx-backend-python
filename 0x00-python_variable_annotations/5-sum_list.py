#!/usr/bin/env python3
""" Module defining type annotated function sum_list. """
from typing import List


def sum_list(input_list: List) -> float:
    """ Function that adds elements of a list. """
    return sum(input_list)
