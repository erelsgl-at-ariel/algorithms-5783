#!python3

"""
Using cvxpy to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import cvxpy, numpy as np

wa = 10
wb = 90 

# Values A
v1a = 40    # Agent A (low weight) gets this.
v2a = 60

# Values B
v1b = 30
v2b = 70    # Agent B (high weight) gets this.

print(f" v1a/wa+v2b/wb={v1a/wa+v2b/wb}\n v2a/wb+v1b/wa={v2a/wb+v1b/wa}")

RENT = 0

p1, p2 = cvxpy.Variable(2)

prob = cvxpy.Problem(
    cvxpy.Minimize(0),
    # cvxpy.Maximize(price_martef+price_heder+price_salon),
    constraints = [p1+p2==RENT,
    (v1a-p1)/wa >= (v2a-p2)/wb,  # no weighted envy A
    (v2b-p2)/wb >= (v1b-p1)/wa,  # no weighted envy B
    ]
)
prob.solve()
print("status: ", prob.status)
print(f"rents: 1={np.round(p1.value)}, 2={np.round(p2.value)}")

