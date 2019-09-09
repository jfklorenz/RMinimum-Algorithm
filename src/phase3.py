#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Phase 3
Author: Julian Lorenz
"""
# ==================================================
#   Import
import random

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

