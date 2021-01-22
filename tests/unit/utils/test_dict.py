"""
Test Dict Module
"""

# Modules
from src.utils import dict_module


def test_all_data_to_int():
    """
    Test all data to int
    """
    data = [
        {'a': '2', 'b': '3'},
        {'a': '2', 'b': '3'},
        {'a': '2', 'b': '3'},
    ]
    expect = [
        {'a': 2, 'b': 3},
        {'a': 2, 'b': 3},
        {'a': 2, 'b': 3},
    ]
    assert dict_module.all_data_to_int(data) == expect
