#!python3

"""
Using scipy.linprog to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

from scipy.optimize import linprog

print("\nFinding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:")


result = linprog(  # variables: price_heder, m, price_salon
    [0, 0, 0], # we do not minimize anything

    # envy-freeness conditions on price_heder, m, price_salon:
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

    # price_heder+m+price_salon=100
    A_eq=[
        [1,1,1]
    ],
    b_eq=[
        100
    ],
    bounds=[(0,None), (0,None), (0,None)]  # price_heder>=0, m>=0, price_salon>=0
    )
print(result.message)
print("Optimal value: ",result.fun)
print("Rent values: [price_heder, price_martef, price_salon] = ",result.x)
print()

#
# print("\nFinding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}")
# m, price_heder, price_salon = cvxpy.Variable(),cvxpy.Variable(), cvxpy.Variable()
# prob = cvxpy.Problem(
#     cvxpy.Maximize(1),
#         constraints = [m+price_heder+price_salon==100,
#             35-price_salon >= 60-price_heder, 35-price_salon >= 40-m,  # aya
#             40-price_heder >= 35-price_salon, 40-price_heder >= 25-m,  # batya
#             20-price_martef >= 40-price_heder, 20-price_martef >= 25-price_salon,  # gila
#             ]
# )
# prob.solve()
# print("status: ", prob.status)
# print("rents: martef={}, heder={}, salon={}".format(m.value,price_heder.value,price_salon.value))
#


import itertools


