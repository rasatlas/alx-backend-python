#!/usr/bin/env python3
""" Module defining type annotated sum_mixed_list function. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function returning sume of hetrogeneous list elememnts. """
    return sum(mxd_lst)
