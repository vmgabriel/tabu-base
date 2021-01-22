"""
Test Handle
"""

# Libraries
# from unittest.mock import Mock


# Modules
from src.app import input_assignation
from src.exceptions import input_exception


def test_pytest():
    """First test of pytest"""
    _x = 1
    _y = 2
    res = _x + _y
    assert res == 3


def test_input_assignation(mocker):
    """Test Input Assignation"""
    mocks_control = [
        ('t', True),
        ('f', True),
        ('n', False),
        ('7', False),
    ]
    for data, wait_response in mocks_control:
        load = False
        mocker.patch(
            'builtins.input',
            lambda x: data
        )
        try:
            assign = input_assignation()
            load = assign == data
        except input_exception.InvalidInput:
            pass

        assert load == wait_response
