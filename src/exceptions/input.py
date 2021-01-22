"""
Control input exception
"""

# Libraries
from typing import Any


class InvalidInput(Exception):
    """
    Control for Invalid input and control in a place
    """
    def __init__(self, _input: Any):
        self._input = _input
        super().__init__(self.message())

    def message(self) -> str:
        """Return error Message"""
        out = '[Input-Error] - {} not valid.'
        return out.format(self._input)
