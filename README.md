# Python-RMinimum

![GitHub status](https://img.shields.io/badge/status-release-success) ![GitHub top language](https://img.shields.io/github/languages/top/jfklorenz/python-rminimum) ![GitHub last commit](https://img.shields.io/github/last-commit/jfklorenz/python-rminimum) ![GitHub](https://img.shields.io/github/license/jfklorenz/python-rminimum)

A **Python** implementation of the **RMinimum algorithm**.

The algorithm is presented in the paper **Fragile Complexity of Comparison-Based Algorithms** by Prof. Dr. Ulrich Meyer and others in 2019.

It introduces the concept of fragile complexity, i.e. the amount of times an element was part of a comparison during the algorithm.

Lets assume a country wants to find its best boxer to represent it during the olypics. If we make a tournament where each loser is eliminated we will evolve with the best boxer, but in a state of exhaustion and maybe even injuries. Therefor it should be the goal to find the best boxer while simultaneously keeping him fit and healthy.

Therefor the RMinimum algorithm finds the minimum element of a given set while being able to control the fragile complexity of its minimum and other elements with a parameter.

---

## data
The **data** folder contains all experimental data as **.csv** files.

---

## docs
The **docs** folder contains the scientific paper presenting the algorithm.

---

## src
The **src** folder contains the source code of the project, i.e.:

| File | Usage |
| ------ | ------ |
| rminimum.py | The entire algorithm |
| phase1.py | The first phase of the algorithm |
| phase2.py | The second phase of the algorithm |
| phase3.py | The third phase of the algorithm |

---

## test
The **test** folder contains multiple tests with **PyTest** and **Jupyter Notebook**.
