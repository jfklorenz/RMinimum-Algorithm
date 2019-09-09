#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Unittest - Phase 3
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import random
import math

# ==================================================
#   Phase 3
def phase3(W, k, M, cnt):
    """
    Phase 3 of the RMinimum algorithm. It takes the winner set from phase 1 and generates n/2k subsets each of size k.
    Then it filters out all elements in each subset that is larger than the respective element from the
    tournament winner set from phase 2, then merges all subsets.

    :param W: Winner set from phase 1
    :type W: List
    :param k: Tuning parameter responsible for the size and amout of subsets
    :type k: INT
    :param M: Tournament winner set from phase 2
    :type M: List
    :param cnt: Saves the fragile complexity for each element
    :type cnt: List

    :return: Wnew, cnt
    :param Wnew: Set of merged subsets with elements smaller than its respective filter element
    :type Wnew: List
    """

    # Generate subsets
    random.shuffle(W)
    W_i = [W[i * k:(i + 1) * k] for i in range((len(W) + k - 1) // k)]
    W_i_filt = [0 for _ in range(len(W_i))]

    # Filter subsets
    for i in range(len(W_i_filt)):
        W_i_filt[i] = [elem for elem in W_i[i] if elem < M[i]]
        cnt[M[i]] += len(W_i[i])
        for elem in W_i[i]:
            cnt[elem] += 1

    # Merge subsets
    Wnew = [w for sublist in W_i_filt for w in sublist]

    return Wnew, cnt

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
def test_p3(n, k):
    #   Generating Testcase
    #   X = [0, ..., 3/4 * n - 1, 3/4 * n + n/k, ..., n + n/k]
    #   M = [3/4 * n, ..., 3/4 * n + n/k - 1]

    W = [i for i in range(int(n + math.ceil(n / k)))]
    M = [i for i in range(int(3 / 4 * n), int(3 / 4 * n + math.ceil(n / k)))]

    for m in M:
        if m in W:
            W.remove(m)

    cnt = [0 for _ in range(int(n + math.ceil(n / k)))]

    W_split, W_split_filt, W_filt, cnt = phase3(W, k, M, cnt)

    #   Test
    assert len(W_split) == math.ceil(n / k)                 # The amount of buckets is correct
    assert max(len(w) for w in W_split) == k                # Buckets have the correct size


    for i in range(len(W_split_filt)):
        if W_split_filt[i] == []:
            assert True
        else:
            assert max(W_split_filt[i]) < M[i]              # Filter test: no element in W[i] was larger than the min[i]

    sum = 0
    for i in range(len(M)):
        sum += cnt[M[i]]
    assert math.floor(n/k) * k <= sum <= math.ceil(n/k)*k   # Each min element was compared with each element in W[i]

    for w in W:
        assert cnt[w] == 1                                  # Each element from W was compared once against its respective min element

    return

# ==================================================
