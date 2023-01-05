#!/usr/bin/env python3
""" Complex types - list of floats """

def sum_list(input_list: list) -> float:
    """
    Function to sum the elements of a list
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
