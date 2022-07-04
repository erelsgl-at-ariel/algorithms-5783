#!python3

"""
A demo of maximizing the sum of logarithms -
  when the variables are integers.

This problem is NP-hard, but when the values are small integers, it can be solved efficiently.
"""

import cvxpy
import math
import numpy as np

def feasibility_constraints(Xig:list)->list:
    """
    Generate the feasibility constraints of the given matrix, namely:
    * Each Xig is between 0 and 1;
    * For each g, the sum of Xig is 1.
    :param Xig: a list of lists of variables: Xig[i,g] is the amount of good g given to agent i.
    :return: a list of constraints.
    """
    constraints = []
    num_of_agents = len(Xig)
    num_of_items =  len(Xig[0])
    for g in range(num_of_items):
        constraints.append(1 ==
            sum([Xig[i][g] for i in range(num_of_agents)]))
        for i in range(num_of_agents):
            constraints += [Xig[i][g] >= 0, Xig[i][g] <= 1]
    return constraints

def solve_and_print(objective, constraints:list, Xig:list, integer:bool=False):
    """
    Solve the optimization problem and print the results.

    :param objective the cvxpy maximization objective function.
    :param constraints the cvxpy list of constraints.
    :param Xig: list of lists of cvxpy.Variables.
    :param integer: True of the variables are whole numbers; False if they can be fractional.
    """
    num_of_agents = len(Xig)
    num_of_items =  len(Xig[0])
    prob = cvxpy.Problem(cvxpy.Maximize(objective), constraints)
    prob.solve()
    print("status: ", prob.status)
    print("maximum product: ", round(math.exp(prob.value),1))
    print("allocation:")
    for i in range(num_of_agents):
        for g in range(num_of_items):
            if integer:
                if Xig[i][g].value > 0.5:
                    print("  agent {} gets item {}".format(i, g))
            else:
                print("  agent {} gets {} of item {}".format(i, np.round(Xig[i][g].value, 2), g))



def max_product_1(value_matrix: list, integer=False):
    """
    Calculate an allocation that maximizes the product of utilities (sum of logs): basic formulation.

    >>> max_product_1([[6,6,0],[0,0,2]])
    status:  optimal
    optimal value:  24.0
    allocation:
    agent 0 gets 1.0 of item 0
    agent 0 gets 1.0 of item 1
    agent 0 gets 0.0 of item 2
    agent 1 gets 0.0 of item 0
    agent 1 gets 0.0 of item 1
    agent 1 gets 1.0 of item 2
    >>> max_product_1([[6,2,7],[1,5,7]])
    status:  optimal
    optimal value:  81.0
    allocation:
    agent 0 gets 1.0 of item 0
    agent 0 gets 0.0 of item 1
    agent 0 gets 0.43 of item 2
    agent 1 gets 0.0 of item 0
    agent 1 gets 1.0 of item 1
    agent 1 gets 0.57 of item 2

    :param value_matrix: list of lists.
    :return: allocation that maximizes the sum of logs.
    """

    num_of_agents = len(value_matrix)
    num_of_items =  len(value_matrix[0])
    Xig = [[cvxpy.Variable(integer=integer)
            for _ in range(num_of_items)]
            for _ in range(num_of_agents)]   # Xig[i][g] represents the fraction of good g given to agent i. Should be in {0,1}.

    objective = 0
    constraints = feasibility_constraints(Xig)
    for i in range(num_of_agents):
        value_of_i = sum([Xig[i][g] * value_matrix[i][g]
                          for g in range(num_of_items)])
        objective += cvxpy.log(value_of_i)
    solve_and_print(objective, constraints, Xig, integer)

def max_product_2(value_matrix: list, integer=False):
    """
    >>> max_product_2([[6,6,0],[0,0,2]])
    status:  optimal
    optimal value:  24.0
    allocation:
    agent 0 gets 1.0 of item 0
    agent 0 gets 1.0 of item 1
    agent 0 gets 0.0 of item 2
    agent 1 gets 0.0 of item 0
    agent 1 gets 0.0 of item 1
    agent 1 gets 1.0 of item 2
    >>> max_product_2([[6,2,7],[1,5,7]])
    status:  optimal
    optimal value:  81.0
    allocation:
    agent 0 gets 1.0 of item 0
    agent 0 gets 0.0 of item 1
    agent 0 gets 0.43 of item 2
    agent 1 gets 0.0 of item 0
    agent 1 gets 1.0 of item 1
    agent 1 gets 0.57 of item 2

    :param value_matrix: list of lists.
    :return: allocation that maximizes the sum of logs.
    """

    num_of_agents = len(value_matrix)
    num_of_items =  len(value_matrix[0])
    Xig = [[cvxpy.Variable(integer=integer) for _ in range(num_of_items)] for _ in range(num_of_agents)]   # Xig[i][g] represents the fraction of good g given to agent i. Should be in {0,1}.

    Wi = [cvxpy.Variable() for _ in range(num_of_agents)]                                                # Wi[i] represents the log of the value of agent i

    objective = sum(Wi)
    constraints = feasibility_constraints(Xig)
    for i in range(num_of_agents):
        value_of_i = sum([Xig[i][g] * value_matrix[i][g] for g in range(num_of_items)])
        constraints.append(Wi[i] <= cvxpy.log(value_of_i))
    solve_and_print(objective, constraints, Xig, integer)



def max_product_3(value_matrix: list, max_value:int, integer=False):
    """
    >>> max_product_3([[6,2,7],[1,5,7]], 10)
    Agent #1 gets items #1, #3
    Agent #2 gets item #2
    Product = 65
    :param value_matrix: list of lists.
    :return: allocation that maximizes the sum of logs.
    """

    num_of_agents = len(value_matrix)
    num_of_items =  len(value_matrix[0])
    Wi = [cvxpy.Variable() for _ in range(num_of_agents)]                                                # Wi[i] represents the log of the value of agent i
    Xig = [[cvxpy.Variable(integer=integer) for _ in range(num_of_items)] for _ in range(num_of_agents)]   # Xig[i][g] represents the fraction of good g given to agent i. Should be in {0,1}.

    objective = sum(Wi)
    constraints = feasibility_constraints(Xig)

    for i in range(num_of_agents):
        value_of_i = sum([Xig[i][g] * value_matrix[i][g] for g in range(num_of_items)])
        for k in range(1,max_value+1):
            constraint_k = Wi[i] <= math.log(k) + (math.log(k+1) - math.log(k))*(value_of_i - k)
            constraints.append(constraint_k)
    solve_and_print(objective, constraints, Xig, integer)


print("\nFormulation 1:")
max_product_1([[6, 6, 0], [0, 0, 2]])
max_product_1([[6, 2, 7], [1, 5, 7]])   # Uri Zitzer's example

print("\nFormulation 2:")
max_product_2([[6, 6, 0], [0, 0, 2]])
max_product_2([[6, 2, 7], [1, 5, 7]])

print("\nFormulation 3, integers")
max_product_3([[6, 6, 0], [0, 0, 2]], 10, integer=True)
max_product_3([[6, 2, 7], [1, 5, 7]], 10, integer=True)






"""
From Mathematica:

FindMaximum[{W1 + W2 + W3,
  W1 <= Log[1] + (Log[2] - Log[1])*(81 x + 19 - 1),
  W1 <= Log[2] + (Log[3] - Log[2])*(81 x + 19 - 2),
  W1 <= Log[3] + (Log[4] - Log[3])*(81 x + 19 - 3),
  W1 <= Log[4] + (Log[5] - Log[4])*(81 x + 19 - 4),
  W1 <= Log[5] + (Log[6] - Log[5])*(81 x + 19 - 5),
  W1 <= Log[6] + (Log[7] - Log[6])*(81 x + 19 - 6),
  W2 <= Log[1] + (Log[2] - Log[1])*(80 y + 20 - 1), 
  W2 <= Log[2] + (Log[3] - Log[2])*(80 y + 20 - 2), 
  W2 <= Log[3] + (Log[4] - Log[3])*(80 y + 20 - 3), 
  W2 <= Log[4] + (Log[5] - Log[4])*(80 y + 20 - 4), 
  W2 <= Log[5] + (Log[6] - Log[5])*(80 y + 20 - 5), 
  W2 <= Log[6] + (Log[7] - Log[6])*(80 y + 20 - 6), 
  W3 <= Log[1] + (Log[2] - Log[1])*(60 z + 40 - 1), 
  W3 <= Log[2] + (Log[3] - Log[2])*(60 z + 40 - 2), 
  W3 <= Log[3] + (Log[4] - Log[3])*(60 z + 40 - 3), 
  W3 <= Log[4] + (Log[5] - Log[4])*(60 z + 40 - 4), 
  W3 <= Log[5] + (Log[6] - Log[5])*(60 z + 40 - 5), 
  W3 <= Log[6] + (Log[7] - Log[6])*(60 z + 40 - 6), 
  0 <= x <= 1, 0 <= y <= 1, 0 <= z <= 1, x + y + z == 1, 
  Element[{x, y, z}, Integers]}, {W1, W2, W3, x, y, z}]

"""
