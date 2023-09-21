"""Module for computing the longest increasing subsequence."""

from typing import Sequence, Any


def is_increasing(x: Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.

    >>> is_increasing([1, 4, 6])
    True
    >>> is_increasing("abc")
    True
    >>> is_increasing("cba")
    False
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True


def liseq(x: Sequence[Any]) -> list[int]:
    """
    Compute a longest increasing subsequence.

    Return the sequence as a list of indices.

    >>> liseq([12, 45, 32, 65, 78, 23, 35, 45, 57])
    [0, 5, 6, 7, 8]
    """
    best: list[int] = []
    # Explore all alternatives
    """Finding increasing substrings"""
    increasing_substrings = []
    for i in range(len(x)-1):
        accumulator = 0
        for j in range(i+1, len(x)+1):
            increasing = is_increasing(x[i+accumulator:j+1])
            if increasing == True:
                accumulator += 1
                increasing_substrings.append((i,j))
                continue
            else:
                break
    """Finding longest increasing substring"""
    lengths = []
    for i in increasing_substrings:
        lengths.append(i[1] - i[0])
    longest = increasing_substrings[lengths.index(max(lengths))]
    best = list(range(longest[0], longest[1]))
    # best = [x[i] for i in best_indexes], to get the values in the longest increasing subsequence
    return best

print(liseq([12, 45, 32, 65, 78, 23, 35, 45, 57]))