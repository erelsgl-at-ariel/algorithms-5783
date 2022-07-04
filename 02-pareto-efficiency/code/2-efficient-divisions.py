#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

print("\n\n\nPROBLEM #1")
print("A cake with three regions (Wood, Oil, Steel) has to be divided among two people with values:")
print("80 19 1")
print("70 1 29")

x, y, z = cvxpy.Variable(3)   # fractions of the three regions given to Ami

utility_ami = x*80 + y*19 + z*1
utility_tami = (1-x)*60 + (1-y)*1 + (1-z)*39 

print("\nUtilitarian division - maximum sum of utilities:")

prob = cvxpy.Problem(
    cvxpy.Maximize(utility_ami + utility_tami),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", x.value, y.value, z.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)


print("\nAttempt 2 - maximize the sum of roots:")
prob = cvxpy.Problem(
    cvxpy.Maximize(utility_ami**0.5 + utility_tami**0.5),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("Fractions given to Ami: ", x.value, y.value, z.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)


print("\nEgalitarian division")

min_utility = cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1, 
                   min_utility<=utility_ami, min_utility<=utility_tami])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", x.value, y.value, z.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)

