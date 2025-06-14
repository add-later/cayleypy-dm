"""Helper functions."""
from typing import Any, Sequence, Tuple, List


def apply_permutation(p: Any, x: Sequence[Any]) -> list[Any]:
    return [x[p[i]] for i in range(len(p))]


def compose_permutations(p1: Sequence[int], p2: Sequence[int]) -> list[int]:
    """Returns p1∘p2."""
    return apply_permutation(p1, p2)


def inverse_permutation(p: Sequence[int]) -> list[int]:
    n = len(p)
    ans = [0] * n
    for i in range(n):
        ans[p[i]] = i
    return ans


def is_permutation(p):
    return sorted(list(p)) == list(range(len(p)))


def all_transpositions(n: int) -> Tuple[List[List[int]], List[str]]:
    """
    Returns all transpositions (single swaps) of n numbers (counting from 0) and list or string.
    Example:
    transpositions(4) returns
    [
        [1, 0, 2, 3], [2, 1, 0, 3],
        [3, 1, 2, 0], [0, 2, 1, 3],
        [0, 3, 2, 1], [0, 1, 3, 2]
    ]
    ['(0,1)', '(0,2)', '(0,3)', '(1,2)', '(1,3)', '(2,3)'])
    """
    result = []
    names = []
    for i in range(n):
        for j in range(i+1, n):
            p = list(range(n))
            p[i], p[j] = p[j], p[i]
            result.append(p)
            names.append(f"({i},{j})")
    assert len(result) == n * (n-1) // 2
    return result, names
