"""
Demonstrates using ILP to solve maximum matching in python.
Programmer: Erel Segal-Halevi
Since: 2023-01
"""


import networkx as nx
import cvxpy

e = cvxpy.Variable(9, integer=True)
range_constraints = [x >= 0 for x in e]  + [x <= 1 for x in e]

capacity_constraint = [
    # for each vertex v there is at most one outgoing edge:
    e[1] <= 1,       # v1
    e[2]+e[3] <= 1,  # v2
    e[4]+e[5] <= 1,  # v3
    e[6]+e[7] <= 1,  # v4
    e[8] <= 1,       # v5
]

matching_constraints = [
    # for each vertex v, if there is an outgoing edge, then there is an incoming edge:
    e[1] == e[2]+e[8],       # v1
    e[2]+e[3] == e[4]+e[1],  # v2
    e[4]+e[5] == e[6]+e[3],  # v3
    e[6]+e[7] == e[5],  # v4
    e[8] == e[7],       # v5
]

prob = cvxpy.Problem(
    cvxpy.Maximize(sum(e)),
    constraints = range_constraints + capacity_constraint + matching_constraints + [e[0]==0])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("edges: ", [(i, e[i].value) for i in range(9)])

no_long_paths_constraints = [
    # For every path of length 3 (that is not a cycle), at most two edges are chosen.
    e[1]+e[3]+e[5] <= 2,
    e[3]+e[5]+e[7] <= 2,
    e[5]+e[7]+e[8] <= 2,
    e[7]+e[8]+e[1] <= 2,
    e[8]+e[1]+e[3] <= 2,
    e[6]+e[4]+e[2] <= 2,
]

prob = cvxpy.Problem(
    cvxpy.Maximize(sum(e)),
    constraints = range_constraints + capacity_constraint + matching_constraints + no_long_paths_constraints + [e[0]==0])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("edges: ", [(i, e[i].value) for i in range(9)])
