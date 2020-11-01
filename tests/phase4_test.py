#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 4
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import random
import queue
import math

# ==================================================
#   Phase 4
def phase4(Wnew, k, n0, cnt):
    """
    Phase 4 of the RMinimum algorithm. It checks if the number of elements in Wnew is smaller than the
    logarithmic value of the original input size squared.
    If that is the case it determines the minimum element from the set Wnew with a perfectly balanced tournament tree.
    Otherwise it calls the entire algorithm with the new set Wnew.

    :param Wnew: Set of filtered winners from phase 3
    :type Wnew: List
    :param k: Tuning parameter responsible for the size and amout of subsets
    :type k: INT
    :param n0: Size of the original input set of the algorithm
    :type n0: INT
    :param cnt: Saves the fragile complexity for each element
    :type cnt: List

    :return: mini, cnt, rec OR recursive call with Wnew as the new input set
    :param mini: The minimum element of the set Wnew
    :type mini: INT
    """

    # Recursive call check
    if len(Wnew) <= math.log(n0, 2) ** 2:
        q = queue.Queue()

        for ele in Wnew:
            q.put(ele)
        while q.qsize() > 1:
            a = q.get()
            b = q.get()

            if a < b:
                q.put(a)
            else:
                q.put(b)

            cnt[a] += 1
            cnt[b] += 1
        mini = q.get()

        return mini, cnt

    else:
        return -1, cnt

# ==================================================
#   Unittest : Parameter
@pytest.mark.parametrize(('n','n0'), [
    #   Manuel input
    (2**10, 2**5), (2**16, 2**8 + 1),                  # |W'| < log2(n0)**2
    (2**10, 100), (2**16, 2**8),                       # |W'| = log2(n0)**2
    (2**10, 2**2), (2**16, 2**8 - 1)                   # |W'| > log2(n0)**2
])
# ==================================================
#   Unittest : Test
def test_p4(n, n0):
    #   Generating Testcase
    newW = [i for i in range(n)]
    cnt = [0 for _ in range(n)]

    mine, cnt = phase4(newW, 16, n0, cnt)

    #   Test
    if n > (math.log(n0) / math.log(2))**2:             # Recursive call
        assert mine == -1
    else:
        assert min(newW) == mine                        # The minimum was indeed found
        assert max(cnt) <= math.log(n) / math.log(2)    # max count is bound by log2(|W|)
        assert sum(cnt) == n - 1                        # Each compare kicks one element out of the tournament tree

# ==================================================
