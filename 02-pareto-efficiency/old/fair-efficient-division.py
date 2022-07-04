#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

print("\n\n\nPROBLEM #1")
print("A cake with three regions has to be divided among two people with values:")
print("19 0 81")
print("0 20 80")

# Define x = the fraction of the third region given to the first agent.
x = cvxpy.Variable()

print("\nAttempt 1: find a sum-maximizing division:")
prob = cvxpy.Problem(
    cvxpy.Maximize((81*x + 19) + (80*(1-x)+20)),
    constraints = [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("value of Ami", 81*x.value+19)
print("value of Tami", 80*(1-x.value)+20)


print("\nAttempt 2: maximize the sum of roots:")
prob = cvxpy.Problem(
    cvxpy.Maximize((81*x + 19)**0.5 + (80*(1-x)+20)**0.5),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("value of Ami", 81*x.value+19)
print("value of Tami", 80*(1-x.value)+20)


print("\nAttempt 3: maximize the sum of logs:")
from cvxpy import log
prob = cvxpy.Problem(
    cvxpy.Maximize(log(81*x + 19) + log(80*(1-x)+20)),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("value of Ami", 81*x.value+19)
print("value of Tami", 80*(1-x.value)+20)

x = cvxpy.Variable()
y = cvxpy.Variable()

print("\n\n\nPROBLEM #2")
print("A cake with four regions has to be divided among 3 people with values:")
print("19 0 0 81")
print("0 20 0 80")
print("0 0 40 60")

# Define x,y,z = the fraction of the fourth region given to agents 1,2,3.
x = cvxpy.Variable()
y = cvxpy.Variable()
z = cvxpy.Variable()

print("\nMaximize the sum of logs:")
prob = cvxpy.Problem(
    objective   =  cvxpy.Maximize(log(81*x + 19) + log(80*y+20) + log(60*z+40)),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1, x+y+z == 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("optimal y", y.value)
print("optimal z", z.value)




t = 0.51
print("\nAttempt 2: maximize the sum of roots:")
prob = cvxpy.Problem(
    cvxpy.Maximize((x)**0.5 + (1-t*x)**0.5),
    [0 <= x, x <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal x", x.value)
print("value of Ami", x.value)
print("value of Tami", (1-t*x.value))
