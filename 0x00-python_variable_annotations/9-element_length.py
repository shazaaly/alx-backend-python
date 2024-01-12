
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Takes a list of strings and returns a list of tuples
    where each tuple is a string from the list and its length.
    """

    return [(i, len(i)) for i in lst]
