"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

fractions  = cvxpy.Variable((3,3))
values = [
    
]

utility_ami =  salonx*80 + y*19 + z*1
utility_tami = (1-x)*60 + (1-y)*1 + (1-z)*39 
utility_rami = 

print("\nMaximize the sum of logs:")
prob = cvxpy.Problem(
    cvxpy.Maximize(cvxpy.log(utility_ami) + cvxpy.log(utility_tami)),
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

