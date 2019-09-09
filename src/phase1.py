#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Phase 1
Author: Julian Lorenz
"""
# ==================================================
#   Import
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
