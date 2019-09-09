#!/usr/bin/python3
# ==================================================
"""
File: RMinimum - Full Algorithm
Author: Julian Lorenz
"""
# ==================================================
#   Import
import pytest
import math
import random
import queue

# ==================================================
#   RMinimum
def rminimum(X, k, cnt = [], rec = 0):

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
def test_algo(n, k):
    #   Generating Testcase
    X = [i for i in range(n)]

    minE, cnt = rminimum(X, k)

    work = sum(cnt) / 2

    #   Test
    assert minE == 0                            # Minimum was indeed found
    assert n / 2 <= work <= 2 * n               # work linear with factor in [1/2, 2]

    return

# ==================================================
