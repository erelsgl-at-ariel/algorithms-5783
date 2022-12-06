#!python3

"""
Using cvxpy to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import cvxpy, numpy as np


print("\nFinding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:")

price_martef, price_heder, price_salon = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Minimize(0),
    # cvxpy.Maximize(price_martef+price_heder+price_salon),
    constraints = [price_martef + price_heder + price_salon == 1000,
                   # price_martef >= 0, price_heder >= 0, price_salon >= 0,
            350 - price_salon >= 400 - price_heder,
            350 - price_salon >= 250 - price_martef,  # aya does not envy

            600 - price_heder >= 350 - price_salon,
            600 - price_heder >= 400 - price_martef,  # batya does not envy

            200 - price_martef >= 400 - price_heder,
            200 - price_martef >= 250 - price_salon,  # gila does not envy
    ]
)
prob.solve()
print("status: ", prob.status)
print("optimal value: ", prob.value)
print(f"rents: heder={np.round(price_heder.value)}, martef={np.round(price_martef.value)}, salon={np.round(price_salon.value)}")


print("\nFinding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}")
price_martef, price_heder, price_salon = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Minimize(0),
    constraints = [
            price_martef + price_heder + price_salon == 100,
            40 - price_heder >= 35 - price_salon, 40 - price_heder >= 25 - price_martef,  # aya
            35 - price_salon >= 60 - price_heder, 35 - price_salon >= 40 - price_martef,  # batya
            20 - price_martef >= 40 - price_heder, 20 - price_martef >= 25 - price_salon,  # gila
                   ]
)
prob.solve()
print("status: ", prob.status)
print("optimal value: ", prob.value)
print("rents: heder={}, martef={}, salon={}".format(price_heder.value, price_martef.value, price_salon.value))
