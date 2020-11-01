#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Phase 2
Author: Julian Lorenz
"""
# ==================================================
#   Import
import random
import queue

# ==================================================
#   Phase 2
def phase2(L, k, cnt):
    """
    Phase 2 of the RMinimum algorithm takes the loser set from phase 1 and generates n/2k subsets each of size k,
    after which it determines the smallest element of each subset using a perfectly balanced tournament tree.

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

L = [i for i in range(1024)]
k = 16
cnt = [0 for _ in range(1024)]
print(phase2(L, k, cnt))
