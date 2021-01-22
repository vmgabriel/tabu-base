"""
Module for app - load
"""

# Libraries
import sys

# Exceptions
from src.exceptions import input_exception


def input_assignation():
    """
    read input assignation

    if not valid assign input this send Exception based in InvalidInput
    """
    tabu_input = input('Tabu Aspiration\n(t)rue\n(f)alse\n# ')
    if tabu_input not in ['t', 'f']:
        raise input_exception.InvalidInput(tabu_input)
    return tabu_input


def run():
    """Load process for app"""
    try:
        if input_assignation() == 't':
            print('T')
        else:
            print('F')
    except input_exception.InvalidInput as _a:
        print(f'data - {_a}')
