"""
Dict Utils Module
"""

# Libraries
from typing import List

# Modules
from src.utils.composer import composer


def to_items(dict_data: dict) -> List[tuple]:
    """To item"""
    return dict_data.items()


def all_data_to_int(data: List[dict]) -> List[dict]:
    """
    Convert a List of dicts with data str to List of dicts with data int
    """

    def value_to_int(key: str, value: str) -> tuple:
        """Convert Second value to int"""
        return (key, int(value))

    def convert_all_to_int(tuple_data: List[tuple]) -> List[tuple]:
        """Convert all to int"""
        if len(tuple_data) == 0:
            return []
        head, *tail = tuple_data
        return [value_to_int(*head)] + convert_all_to_int(tail)

    return list(map(
        composer(
            dict,
            convert_all_to_int,
            to_items
        ),
        data
    ))
