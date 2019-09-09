#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Phase 4
Author: Julian Lorenz
"""
# ==================================================
#   Import
import queue
import math

# ==================================================
#   Phase 4
#   Returns -1 for the minimum element in case of a recursive call
def phase4(Wnew, k, n0, cnt, rec):
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
    :param rec: Current count of recursive calls made already
    :type rec: INT

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

        return mini, cnt, rec

    else:
        rec += 1
        return -1, cnt, rec

# ==================================================