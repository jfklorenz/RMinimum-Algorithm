#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Full Algorithm
Author: Julian Lorenz
"""
# ==================================================
#   Import
import math
import random
import queue

# ==================================================
#   Input transformation
def inp(X):
    """
     Allows to parameterize RMinimum with an INT or a list.
     Automatically generates a list from the first X numbers, i.e. [0, ..., X-1].

    :param X: Either an INT or a list
    :return: list = [0,...,X] when X is INT, otherwise it returns X
    """
    try:
        return [i for i in range(X)]
    except ValueError:
        return X

# ==================================================
#   RMinimum
def rminimum(X, k, cnt = [], rec = 0):
    """
    RMinimum finds the minimum element within a total ordered set of elements.
    During the process it saves the fragile complexity for each element and the number of recursive calls.

    The elements of the input set must be INT and the number of elements must be even.

    :param X: Either a total ordered set of elements or an INT to create such a list with |X| mod(2) = 0.
    :type X: INT or list
    :param k: tuning paramenter, regulating the fragile complexity
    :type k: INT
    :param cnt: Saves the fragile complexity for each element
    :type cnt: List
    :param rec: Number of recursive calls
    :type rec: INT

    :return: mini, cnt, rec
    :param mini: Minimum element of the given set
    :type mini: INT
    """

    # Check input
    X = inp(X)

    # Generate empty cnt list if its not a recursive call
    if cnt == []:
        cnt = [0 for _ in range(max(X) + 1)]

    # Convert parameters if needed
    k = int(k)
    n = len(X)

    # Base case |X| = 3
    if len(X) == 3:
        if X[0] < X[1]:
            cnt[X[0]] += 2
            cnt[X[1]] += 1
            cnt[X[2]] += 1

            if X[0] < X[2]:
                mini = X[0]
            else:
                mini = X[2]
        else:
            cnt[X[0]] += 1
            cnt[X[1]] += 2
            cnt[X[2]] += 1

            if X[1] < X[2]:
                mini = X[1]
            else:
                mini = X[2]
        return mini, cnt, rec

    # Run phases
    W, L, cnt = phase1(X, cnt)
    M, cnt = phase2(L, k, cnt)
    Wnew, cnt = phase3(W, k, M, cnt)
    mini, cnt, rec = phase4(Wnew, k, n, cnt, rec)

    return mini, cnt, rec

# --------------------------------------------------
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

# --------------------------------------------------
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

# --------------------------------------------------
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

# --------------------------------------------------
#   Phase 4
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
        return rminimum(Wnew, k, cnt, rec)

# ==================================================

mini, cnt, rec = rminimum(4, 2)
print(mini)