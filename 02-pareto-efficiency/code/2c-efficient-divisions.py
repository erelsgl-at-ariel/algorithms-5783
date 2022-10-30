#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find an egalitarian division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

print("\n\n\nPROBLEM #1")
print("Three resources (Wood, Oil, Steel) has to be divided among two people with values:")
print("80 19 1")
print("60 1 39")

xw, xo, xs = cvxpy.Variable(3)   # fractions of the three regions given to Ami

utility_ami = xw*80 + xo*19 + xs*1
utility_tami = (1-xw)*60 + (1-xo)*1 + (1-xs)*39

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


print("\nAttempt 2 - maximize the sum of roots:")
prob = cvxpy.Problem(
    cvxpy.Maximize(utility_ami**0.5 + utility_tami**0.5),
    constraints = [0 <= xw, xw <= 1, 0 <= xo, xo <= 1, 0 <= xs, xs <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("Fractions given to Ami: ", xw.value, xo.value, xs.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)

print("\nAttempt 3 - maximize the sum of logarithms:")
prob = cvxpy.Problem(
    cvxpy.Maximize(cvxpy.log(utility_ami) + cvxpy.log(utility_tami)),
    constraints = [0 <= xw, xw <= 1, 0 <= xo, xo <= 1, 0 <= xs, xs <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("Fractions given to Ami: ", xw.value, xo.value, xs.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)


print("\nEgalitarian division")

min_utility = cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = [0 <= xw, xw <= 1, 0 <= xo, xo <= 1, 0 <= xs, xs <= 1, 
                   min_utility<=utility_ami, min_utility<=utility_tami])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", xw.value, xo.value, xs.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)

