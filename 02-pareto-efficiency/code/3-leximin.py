#!python3

"""
Using cvxpy - the contex optimization package of Python -
to find a leximin-egalitarian ditision.

AUTHOR: Erel Segal-Haleti
SINCE:  2021-10
"""

import cvxpy


x = cvxpy.Variable(4)  # fraction of iron
y = cvxpy.Variable(4)  # fraction of oil
z = cvxpy.Variable(4)  # fraction of wood

utilities = [x[0]*4, y[1]*3, x[2]*5+y[2]*5+z[2]*10, x[3]*5+y[3]*5+z[3]*10]

fixed_constraints = \
    [0<=t for t in x] + [t<=1 for t in x] + \
    [0<=t for t in y] + [t<=1 for t in y] + \
    [0<=t for t in z] + [t<=1 for t in z] + \
    [sum(x)==1, sum(y)==1, sum(z)==1]

print("\n1. Egalitarian division")

min_utility = cvxpy.Variable()  # the minimum utility 
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = fixed_constraints + [min_utility <= u for u in utilities])
prob.solve()
print("optimal value: ", prob.value)
print("Utilities: ", [u.value for u in utilities])

for player in range(len(utilities)):
    print(f"   Checking the max utility of {player}:")
    prob = cvxpy.Problem(
        cvxpy.Maximize(utilities[player]),
        constraints = fixed_constraints + [u >= 3 for u in utilities])
    prob.solve()
    print("   optimal value: ", prob.value)
    print(f"   iron: {x.value.round(2)},\n oil: {y.value.round(2)},\n wood: {z.value.round(2)}")

print("\n2. Egalitarian division with saturated player")

min_utility = cvxpy.Variable()  # the minimum utility 
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = fixed_constraints + [min_utility<=utilities[0], min_utility<=utilities[2], min_utility<=utilities[3], utilities[1]==3])
prob.solve()
print("optimal value: ", prob.value)
print("Utilities: ", [u.value for u in utilities])

