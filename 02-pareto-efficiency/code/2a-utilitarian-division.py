#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find an efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

print("\n\n\nPROBLEM #1")
print("Three resources (Wood, Oil, Steel) has to be divided among two people with values:")
print("80 19 1")
print("79 1 20")

xw, xo, xs = cvxpy.Variable(3)   # fractions of the three resources given to Ami

utility_ami  = xw*80 + xo*19 + xs*1
utility_tami = (1-xw)*79 + (1-xo)*1 + (1-xs)*20

print("\nUtilitarian division - maximum sum of utilities:")

prob = cvxpy.Problem(
    cvxpy.Maximize(utility_ami + utility_tami),
    constraints = [0 <= xw, xw <= 1, 0 <= xo, xo <= 1, 0 <= xs, xs <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", xw.value, xo.value, xs.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)
