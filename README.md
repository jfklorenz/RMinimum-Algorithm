# RMinimum-Algorithm

![GitHub status](https://img.shields.io/badge/status-release-success) ![GitHub top language](https://img.shields.io/github/languages/top/jfklorenz/python-rminimum) ![Travis](https://travis-ci.org/jfklorenz/RMinimum-Algorithm.svg?branch=master)
[![PyPI version](https://badge.fury.io/py/RMinimum-Algorithm.svg)](https://badge.fury.io/py/RMinimum-Algorithm) ![Liscence](https://img.shields.io/github/license/jfklorenz/RMinimum-Algorithm)

A **Python** implementation of the **RMinimum algorithm**.

The algorithm is presented in the paper **Fragile Complexity of Comparison-Based Algorithms** by Prof. Dr. Ulrich Meyer and others in 2018.
A reworked version can can be found on [arXiv.org](https://arxiv.org/abs/1901.02857 "arXiv.org").

It introduces the algorithms *RMinimum* and *RMedian* and also the concept of *fragile complexity*, i.e. the amount of times an element has been compared during the process of the algorithm.

Folder | Content
--- | ---
data | all experimental data as *.csv* files
docs | scientific paper presenting the algorithm (old & new version)
jupyter | *Jupyter Notebook* validation and test files  
src | *Python* source code
tests | *PyTest* test files

The package was published on **PyPI** and tested on **Travis CI**.

---

## Algorithm
In the following we present RMinimum, a randomized recursive algorithm for finding the minimum among n distinct elements. The algorithm has a tuning parameter k(n) controlling the
trade-off between the expected fragile complexity f_min(n) of the minimum element and the maximum expected fragile complexity f_rem(n) of the remaining non-minimum elements; if n is clear from the context, we use k instead of k(n). Depending on the choice of k, we obtain interesting trade-offs for the pair <E(f_min(n)) , max E(f_rem(n))> ranging from <O(ε^(−1)*loglog(n)), O(n_ε)> to
<O(log(n)/loglog(n)), O(log(n)/loglog(n))>.

Given a total ordered set X of n distinct elements, RMinimum performs the following steps:

1. Randomly group the elements into n/2 pairwise-disjoint pairs and use one comparison for each pair to partition X into two sets L and W of equal size: W contains all winners, i.e. elements that are smaller than their partner. Set L gets the losers, who are larger than their partner and hence cannot be the global minimum.
2. Partition L into n/k random disjoint subsets L_1 , . . . , L_n/k each of size k and find the minimum element mi in each Li using a perfectly balanced tournament tree (see Theorem 1).
3. Partition W into n/k random disjoint subsets W_1 , . . . , W_n/k each of size k and filter out all elements in W_i larger than mi to obtain W_0 = U_i {w|w ∈ Wi ∧ w < mi }.
4. If |W_0| ≤ log2 (n_0) where n0 is the initial problem size, find and return the minimum using a perfectly balanced tournament tree (see Theorem 1). Otherwise recurse on W_0.

---

## Complexity
1. *Runtime:* RMinimum requires linear work w(n) = O(n).
2. Let k(n) = n_ε for 0 < ε ≤ 1/2. Then RMinimum requires E(f_min(n)) = O(ε−1loglog(n)) comparisons for the minimum and E(f_rem(n)) = O(n_ε) for the remaining elements.
3. Let k(n) = logn/loglogn. Then RMinimum requires E(f_min(n)) = O(log(n)/loglog(n)) comparisons for the minimum and E(f_rem(n)) = O(log(n)/loglog(n)) for the remaining elements.
