#!python3

"""
Demonstration of the fractional-budgeting algorithm maximizing the product of utilities.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""


import cvxpy
import functools

# There are 4 projects, denoted by a, b, c, d.
# The same letters denote the budget allocated to them.
allocations = cvxpy.Variable(3)
a, b, c = allocations

# There are 5 citizens. Their preferences are: ab, ac, ad, bc, a. The total budget is 500 - 100 for each citizen
donations = [3, 3, 3, 3]
utilities = [a, a+b, a+c, b]

sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
positivity_constraints = [v >= 0 for v in allocations]
sum_constraint = [cvxpy.sum(allocations)==sum(donations)]

problem = cvxpy.Problem(
    cvxpy.Maximize(sum_of_logs),
    constraints = positivity_constraints+sum_constraint)
problem.solve()

utility_values = [u.value for u in utilities]
print("BUDGET: a={}, b={}, c={}".format(a.value, b.value, c.value))
print("UTILS : {} + {} + {} + {} = {}".format(*utility_values, sum(utility_values)))
