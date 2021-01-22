"""
Composer function
"""

# Modules
from functools import reduce


def composer(*functions):
    """
    Composer function,
    Art of Wizard

    in_de_dob = compose(
      inc,
      pot,
      dec,
      double
    )

    this build function composer imperative module
    Order:
        ^
       / \\ the read is double, dec pot and inc
        |
    """
    return reduce(
        lambda f, g: lambda x: f(g(x)),
        functions,
        lambda x: x
    )
