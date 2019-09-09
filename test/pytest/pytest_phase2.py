#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 2
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import random
import queue
import math

# ==================================================
#   Phase 2
def phase2(L, k, cnt):
    """
    Phase 2 of the RMinimum algorithm. It takes the loser set from phase 1 and generates n/2k subsets each of size k,.
    Then it determines the smallest element of each subset using a perfectly balanced tournament tree.

    :param L: Set of losers from phase 1
    :type L: List
    :param k: Tuning parameter responsible for the size and amout of subsets
    :type k: INT
    :param cnt: Saves the fragile complexity for each element
    :type cnt: List

    :return: M, cnt
    :param M: Set of tournament winner elements
    :type M: List
    """

    # Generate subsets
    random.shuffle(L)
    subsets = [L[i * k:(i + 1) * k] for i in range((len(L) + k - 1) // k)]

    # Init M
    M = [0 for _ in range(len(subsets))]

    # Perfectly balanced tournament tree using a Queue
    for i in range(len(subsets)):
        q = queue.Queue()

        for ele in subsets[i]:
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
        M[i] = q.get()

    return M, cnt

# ==================================================
#   Unittest : Parameter
@pytest.mark.parametrize(('n', 'k'), [
    #   Randomized input
    (2 * random.randint(2**9, 2**15), random.randint(2, 2**10-1)),      # n in [2^10, 2^16], k in [2, 2^10 - 1]

    #   Manuel input
    (2**10 - 2, 2**5), (2**10 + 2, 2**5),                               # n extreme
    (2**10, 1), (2**10, 2), (2**10, 2**9), (2**10, 2**10 - 1),          # k extreme
    (2**10 - 2, 3), (2**10 + 2, 2**10)                                  # k & n extreme
])
# ==================================================
#   Unittest : Test
def test_p2(n, k):
    #   Generating Testcase
    L = [i for i in range(n)]
    cnt = [0 for _ in range(n)]

    L, M, cnt = phase2(L, k, cnt)

    #   Test
    assert len(L) == math.ceil(n / k)                           # |L| = n / k
    assert max(len(l) for l in L) == k                          # max |L_i| == k
    assert math.floor(math.log(k) / math.log(2)) <= max(cnt) <= math.ceil(math.log(k) / math.log(2))
    # Tournament-Tree winner has log(|L_i|) comparisons
    assert min(cnt) <= 1                                        # Some elements were compared at most once
    for c in cnt:
        assert c <= math.ceil(math.log(k) / math.log(2))        # Each Element was compared at most log(k) times
    for i in range(len(L)):
        assert M[i] == min(L[i])                                # Is the min-element chosen really the min element of the bucket
    return

# ==================================================
