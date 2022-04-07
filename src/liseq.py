"""Module for computing the longest increasing subsequence."""

from typing import Any
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
    for subseq in power(list(range(len(x)))):
        if is_increasing([x[i] for i in subseq]):
            if len(subseq) > len(best):
                best = subseq
    return best


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """
    n = 2**len(x)
    res = []
    for i in range(n):
        bits = format(i, "b").zfill(len(x))
        elements = [i for i, b in enumerate(bits) if b == '1']
        res.append([x[j] for j in elements])
    return res
