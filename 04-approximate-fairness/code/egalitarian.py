"""
Demonstrates finding an egalitarian allocation of discrete objects.
"""

import cvxpy
x, y, z = cvxpy.Variable(3, integer=True)
min_utility = cvxpy.Variable()

utility_ami = x*80 + y*19 + z*1
utility_tami = (1-x)*70 + (1-y)*1 + (1-z)*29 

prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = [0 <= x, x <= 1, 0 <= y, y <= 1, 0 <= z, z <= 1, min_utility <= utility_ami, min_utility <= utility_tami])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", x.value, y.value, z.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)
