"""
Dict Utils Module
"""

# Libraries
from typing import List

# Modules
from src.utils.composer import composer


def to_items(dict_data: dict) -> List[tuple]:
    """
    To item
    ex:
    {'a': 1, 'b': 2} -> [('a',1),('b',2)]
    """
    return dict_data.items()


def all_data_to_int(data: List[dict]) -> List[dict]:
    """
    Convert a List of dicts with data str to List of dicts with data int

    [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}] -> [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    """

    def value_to_int(key: str, value: str) -> tuple:
        """
        Convert Second value to int
        ex:
        ('a','0') -> ('a', 0)
        """
        return (key, int(value))

    def convert_all_to_int(tuple_data: List[tuple]) -> List[tuple]:
        """
        Convert all to int
        ex:
        [('a', '0'), ('b', '1')] -> [('a', 0), ('b', 1)]
        """
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
