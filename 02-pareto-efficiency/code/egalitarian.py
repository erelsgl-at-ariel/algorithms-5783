#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

wood_to_ami = cvxpy.Variable() # How many units of wood are given to Ami.
iron_to_ami = cvxpy.Variable() # How many units of iron are given to Ami.
oil_to_ami  = cvxpy.Variable() # How many units of oil  are given to Ami.

utility_ami  = wood_to_ami*70 + iron_to_ami*30 + oil_to_ami*20
utility_tami = (100-wood_to_ami)*10 + (100-iron_to_ami)*50 + (100-oil_to_ami)*60
min_utility = cvxpy.Variable()

prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = [
        0 <= wood_to_ami, wood_to_ami <= 100, 
        0 <= iron_to_ami, iron_to_ami <= 100, 
        0 <= oil_to_ami, oil_to_ami <= 100, 
        min_utility<=utility_ami,
        min_utility<=utility_tami,
        wood_to_ami==0, iron_to_ami==50, oil_to_ami==100
    ])
prob.solve()
print("Units given to Ami: ", wood_to_ami.value, iron_to_ami.value, oil_to_ami.value)
print("Min utility: ", min_utility.value, utility_ami.value,  utility_tami.value)
