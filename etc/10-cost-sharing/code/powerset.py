"""
Implementation of a power-set iterator, from here:
https://stackoverflow.com/a/18035641/827927
"""

from itertools import chain, combinations

def powerset(iterable):
    """
    >>> list(powerset([1,2,3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

