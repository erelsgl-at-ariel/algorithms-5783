#!python3

"""
Using cvxpy - the contex optimization package of Python -
to find a leximin-egalitarian ditision.

AUTHOR: Erel Segal-Halevi
SINCE:  2021-10
"""

import cvxpy

num_of_players = 4

xw = cvxpy.Variable(num_of_players)  # fractions of wood
xo = cvxpy.Variable(num_of_players)  # fractions of oil
xs = cvxpy.Variable(num_of_players)  # fractions of steel

A=0
B=1
C=2
D=3

utilities = [
    xw[A]*4,                  
    xo[B]*3,                  
    xw[C]*5+xo[C]*5+xs[C]*10, 
    xw[D]*5+xo[D]*5+xs[D]*10] 

fixed_constraints = \
    [0<=t for t in xw] + [t<=1 for t in xw] + \
    [0<=t for t in xo] + [t<=1 for t in xo] + \
    [0<=t for t in xs] + [t<=1 for t in xs] + \
    [sum(xw)==1, sum(xo)==1, sum(xs)==1]

free_players = [A,B,C,D]  # non-saturated players

print("\nITERATION 1: Egalitarian division")

min_utility = cvxpy.Variable()  # the minimum utility 
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = fixed_constraints + [min_utility <= u for u in utilities])
prob.solve()
print("optimal value: ", prob.value)
print("Utilities: ", [u.value for u in utilities])
print(f"  Wood: {xw.value.round(2)},\n  oil: {xo.value.round(2)},\n  steel: {xs.value.round(2)}")

for player in free_players:
    print(f"   Checking the max utility of {player}:")
    prob = cvxpy.Problem(
        cvxpy.Maximize(utilities[player]),
        constraints = fixed_constraints + [u >= 3 for u in utilities])
    prob.solve()
    print("   optimal value: ", prob.value)
    print(f"     wood: {xw.value.round(2)},\n     oil: {xo.value.round(2)},\n     steel: {xs.value.round(2)}")

free_players = [A,C,D]  # player B becomes saturated

print("\nITERATION 2: Egalitarian division with player B saturated:")

min_utility = cvxpy.Variable()  # the minimum utility 
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = fixed_constraints + [
        min_utility <= utilities[A],   
        min_utility <= utilities[C],   
        min_utility <= utilities[D],   
        3 == utilities[B]])             # player B is saturated with saturation value = 3.
prob.solve()
print("optimal value: ", prob.value)
print("Utilities: ", [u.value for u in utilities])

for player in free_players:
    print(f"   Checking the max utility of {player}:")
    prob = cvxpy.Problem(
        cvxpy.Maximize(utilities[player]),
        constraints = fixed_constraints + [
        4 <= utilities[A],         
        4 <= utilities[C],         
        4 <= utilities[D],         
        3 == utilities[B],             # player B is saturated with saturation value = 3.
    ])
    prob.solve()
    print("   optimal value: ", prob.value)
    print(f"     wood: {xw.value.round(2)},\n     oil: {xo.value.round(2)},\n     steel: {xs.value.round(2)}")

free_players = [C,D]   # player A becomes saturated

print("\nITERATION 3: Egalitarian division with players A,B saturated:")

min_utility = cvxpy.Variable()  # the minimum utility 
prob = cvxpy.Problem(
    cvxpy.Maximize(min_utility),
    constraints = fixed_constraints + [
        min_utility <= utilities[C],   
        min_utility <= utilities[D],    
        4 == utilities[A],             # player A is saturated with saturation value = 4.
        3 == utilities[B],             # player B is saturated with saturation value = 3.
    ])
prob.solve()
print("optimal value: ", prob.value)
print("Utilities: ", [u.value for u in utilities])

for player in free_players:
    print(f"   Checking the max utility of {player}:")
    prob = cvxpy.Problem(
        cvxpy.Maximize(utilities[player]),
        constraints = fixed_constraints + [
        5 <= utilities[C],              # player C
        5 <= utilities[D],              # player D 
        4 == utilities[A],              # player A is saturated with saturation value = 4.
        3 == utilities[B],              # player B is saturated with saturation value = 3.
    ])
    prob.solve()
    print("   optimal value: ", prob.value)
    print(f"     wood: {xw.value.round(2)},\n     oil: {xo.value.round(2)},\n     steel: {xs.value.round(2)}")
