#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 1
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import random

# ==================================================
#   Phase 1
def phase1(X, cnt):
    """
    Phase 1 of the RMinimum algorithm. It takes a set of total ordered elements and forms random pairs.
    After comparing both elements it then generates two sets W and L, containing the smaller and larger element respectively.

    :param X: Total ordered set of elements
    :type X: List
    :param cnt: Saves the fragile complexity for each element
    :type cnt: List

    :return: W, L, cnt
    :param W: Set of winner elements, i.e. the smaller element of the comparison
    :type W: List
    :param L: Set of loser elements, i.e. the larger element of the comparison
    :type l: List
    """

    # Init W, L
    W = [0 for _ in range(len(X) // 2)]
    L = [0 for _ in range(len(X) // 2)]

    # Random pairs
    random.shuffle(X)
    for i in range(len(X) // 2):
        if X[2 * i] > X[2 * i + 1]:
            W[i] = X[2 * i + 1]
            L[i] = X[2 * i]
        else:
            W[i] = X[2 * i]
            L[i] = X[2 * i + 1]
        cnt[X[2 * i + 1]] += 1
        cnt[X[2 * i]] += 1

    return W, L, cnt

# ==================================================
#   Unittest : Parameter
#   Only sets with an even number of elements may be chosen as an input.
@pytest.mark.parametrize('n', [
    #   Randomized input
    2 * random.randint(2 ** 9, 2 ** 15),      # n in [2^10, 2^16]

    #   Manuel input
    2**10 - 2, 2**10 + 2                      # n extreme
])
# ==================================================
#   Unittest : Test
def test_p1(n):
    #   Generating Tastcase
    lst = [i for i in range(n)]
    cnt = [0 for _ in range(n)]

    W, L, cnt = phase1(lst, cnt)

    #   Test
    assert not -1 in W              # W filled with elements
    assert not -1 in L              # L filled with elements
    assert max(cnt) == 1            # max cnt == 1
    assert min(cnt) == 1            # min cnt == 1
    assert len(W) == n / 2          # |W| == n/2
    assert len(L) == n / 2          # |L| == n/2
    assert min(min(W, L)) in W      # global min in W
    assert max(max(W, L)) in L      # global max in L
    return

# ==================================================
