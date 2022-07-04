#!python3

"""
A demo of cvxpy - the convex-optimization package of python.
"""

import cvxpy

# Create two scalar optimization variables.
x = cvxpy.Variable()
y = cvxpy.Variable()

# Build two constraints.
constraints = [x + y == 1]

# Build an objective function.
obj = cvxpy.Minimize((x - y)**2)

# Form and solve problem.
prob = cvxpy.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.

print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)


# Form and solve an infeasible problem.
prob = cvxpy.Problem(obj, [x + y == 1, x+y >= 2])
prob.solve()  # Returns the optimal value.

print("\nstatus:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value, y.value)
