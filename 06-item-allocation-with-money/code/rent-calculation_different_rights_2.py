#!python3

"""
Using cvxpy to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import cvxpy, numpy as np

wa = 10
wb = 90 

RENT=1000

v1a, v2a, v1b, v2b = cvxpy.Variable(4)
min_diff = cvxpy.Variable()

prob = cvxpy.Problem(
    objective=cvxpy.Maximize(min_diff),
    constraints=[
        min_diff <= (v2a/wb+v1b/wa) -  (v2b/wb+v1a/wa),
        min_diff <= (v1a/wb+v2b/wa) -  (v1b/wb+v2a/wa),
        v1a >= 0, v1b>=0, v2a>=0, v2b>=0,
        v1a + v2a == RENT,
        v1b + v2b == RENT,
        # min_diff <= 100
    ]
)
prob.solve()
print("status: ", prob.status)
print(f"v1a={np.round(v1a.value)}, v2a={np.round(v2a.value)}")
print(f"v1b={np.round(v1b.value)}, v2b={np.round(v2b.value)}")
print(f"min_diff={np.round(min_diff.value)}")

