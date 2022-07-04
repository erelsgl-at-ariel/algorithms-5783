#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find an allocation that maximizes the product of utilities.

AUTHOR: Erel Segal-Halevi
SINCE:  2020-01
"""

import math, cvxpy
from cvxpy import log

print("\n\n\nPROBLEM #1")
print("A cake with two regions has to be divided among 2 people with values:")
print("2 2")
print("0 4")

# Define x,y,z = the fraction of each region given to player 1.
x, y, z = cvxpy.Variable(3)

print("\nMaximize the sum of logs:")
prob = cvxpy.Problem(
    objective   =  cvxpy.Maximize(log(2*x + 4*y) + log(0*(1-x)+4*(1-y))),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal product", math.exp(prob.value))
print("optimal x", x.value)
print("optimal y", y.value)
