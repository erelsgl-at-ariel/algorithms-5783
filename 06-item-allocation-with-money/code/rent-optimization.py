#!python3

"""
Using cvxpy to find an optimal envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2022-12
"""

import cvxpy, numpy as np

print("\nMatching: {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}")
price_martef, price_heder, price_salon = cvxpy.Variable(), cvxpy.Variable(), cvxpy.Variable()
RENT = 3000


def find_rent(objective, additional_constraints):
    print(f"\nFinding rent with objective [{objective}] and additional constraints {additional_constraints}")
    fixed_constraints = [price_martef + price_heder + price_salon == RENT,
                350 - price_salon >= 400 - price_heder,
                350 - price_salon >= 250 - price_martef,  # aya does not envy

                600 - price_heder >= 350 - price_salon,
                600 - price_heder >= 400 - price_martef,  # batya does not envy

                200 - price_martef >= 400 - price_heder,
                200 - price_martef >= 250 - price_salon,  # gila does not envy
    ]
    prob = cvxpy.Problem(objective, fixed_constraints+additional_constraints)
    prob.solve()
    print(f"rents: heder={np.round(price_heder.value)}, martef={np.round(price_martef.value)}, salon={np.round(price_salon.value)}")


find_rent(cvxpy.Maximize(0), [])
find_rent(cvxpy.Minimize(price_martef), [])
find_rent(cvxpy.Minimize(price_heder), [])
find_rent(cvxpy.Minimize(price_salon), [])
find_rent(cvxpy.Minimize(price_salon**2+price_martef**2+price_heder**2), [])

min_rent = cvxpy.Variable()
find_rent(cvxpy.Maximize(min_rent), [min_rent<=price_martef, min_rent<=price_heder, min_rent<=price_salon])
