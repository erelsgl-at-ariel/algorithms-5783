#!python3

"""
Compare cvxpy to linprog for "rental harmony" calculation

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import cvxpy
from scipy.optimize import linprog
from timeit import timeit

m, h, s = cvxpy.Variable(),cvxpy.Variable(), cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Minimize(0),
    constraints = [m+h+s==100,
            m >= 0, h >= 0, s >= 0,
            35-s >= 40-h, 35-s >= 25-m,  # aya
            60-h >= 35-s, 60-h >= 40-m,  # batya
            20-m >= 40-h, 20-m >= 25-s,  # gila
            ]
)
print(timeit(lambda: prob.solve(), number=100))  # in seconds


def linsolve():
    result = linprog(  # variables: price_heder, price_martef, price_salon
        [0, 0, 0], # we do not minimize anything

        # envy-freeness conditions on price_heder, price_martef, price_salon:
        A_ub=[
            [-1, 0, 1],        [0, -1, 1],
            [1, 0, -1],        [1, -1, 0],
            [-1, 1, 0],        [0, 1, -1],
            ],
        b_ub=[
            -5,     10,
            25,     20,
            -20,    -5,
        ],

        # price_heder+price_martef+price_salon=100
        A_eq=[
            [1,1,1]
        ],
        b_eq=[
            100
        ],
        bounds=[(0,None), (0,None), (0,None)]  # price_heder>=0, price_martef>=0, price_salon>=0
        )
print(timeit(lambda: linsolve(), number=100))  # in seconds

