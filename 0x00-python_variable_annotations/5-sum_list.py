#!/usr/bin/env python3

'''
type-annotated function sum_list which takes a list input_list

'''

from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    return a sum of all nums inside a list

    """
    return sum(input_list)
