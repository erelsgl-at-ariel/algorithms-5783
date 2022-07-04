#!python3

"""
Demonstration of the fractional-budgeting algorithm maximizing the product of utilities.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""


import cvxpy

TOTAL_BUDGET=4000
budget_for_greens  = cvxpy.Variable()
budget_for_reds    = cvxpy.Variable()
budget_for_yellows = cvxpy.Variable()
budget_for_blues   = cvxpy.Variable()

utilities = [
    budget_for_greens+budget_for_reds,  # citizen 1
    budget_for_reds+budget_for_yellows,  # citizen 2
    budget_for_yellows+budget_for_blues,  # citizen 3
    budget_for_reds+budget_for_yellows+budget_for_blues,  # citizen 4
]

sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])

budgets = [budget_for_greens, budget_for_reds, budget_for_yellows, budget_for_blues]
problem = cvxpy.Problem(
    cvxpy.Maximize(sum_of_logs),
    constraints = 
        [v >= 0 for v in budgets] + 
        [cvxpy.sum(budgets)==TOTAL_BUDGET]
        )
problem.solve()

print(f"budgets: greens={budget_for_greens.value}, reds={budget_for_reds.value}, yellows={budget_for_yellows.value}, blues={budget_for_blues.value}")

BUDGET_PER_PERSON = TOTAL_BUDGET / len(utilities)
i=1
print("Citizen {} should donate  {} to the yellows and {} to the reds".format(i,
    budget_for_yellows.value * BUDGET_PER_PERSON / utilities[i].value,
    budget_for_reds.value * BUDGET_PER_PERSON / utilities[i].value
))

