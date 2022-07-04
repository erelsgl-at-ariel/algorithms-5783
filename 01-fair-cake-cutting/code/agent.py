#!python3

"""
Defines an Agent class, that represents an agent in a cake-cutting algorithm.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

from typing import List

class Agent:

    def __init__(self, values:list):
        """
        Initialize an agent with piecewise-constant valuations over a 1-dimensional cake.
        :param values:  The values of the agent to the regions of the cake.
        """
        self.values = values


    def eval(self, x:float, y:float)->float:
        """
        :param    x,y: positive numbers representing locations on the cake.
        :return:  v: the value of the piece [x,y] for the agent.
        """
        pass

    def eval(self, x:float)->float:
        """
        :param    x: a positive number representing a location on the cake.
        :return:  v: the value of the piece [0,x] for the agent.
        """
        pass

    def mark(self, v:float)->float:
        """
        :param    v: a positive number representing a value of a piece.
        :return:  x: a number such that the value of [0,x] equals v.
        """
        pass

def cutAndChoose(a:Agent, b:Agent):
    """
    :param a, b: two agents.
    :return:  prints a fair division of the cake [0,1].

    """
    pass

def lastDiminisher(agents:List[Agent]):
    """
    :param a, b: two agents.
    :return:  prints a fair division of the cake [0,1].

    """
    pass


def plotSimplexOfPartitions(agent:Agent):
    """
    :param agent: an agent with an "eval" function over [0,1].
    Output: a plot of the 2-dimensional partition simplex, where:
      red   = the agent prefers piece #1;
      green = the agent prefers piece #2;
      blue  = the agent prefers piece #3;
    """
    pass