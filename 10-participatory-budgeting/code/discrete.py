#!python3

"""
Demonstration of proportional participatory budgeting algorithm.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-12
"""


from itertools import chain, combinations
import logging, sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

def powerset(iterable:list):
    """
    By Martijn Pieters, from
    From https://stackoverflow.com/a/18035641/827927
    """
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def print_project_sets_by_descending_cost(map_project_to_cost:dict):
    map_project_set_to_cost = lambda ps: sum([map_project_to_cost[p] for p in ps])
    projects = map_project_to_cost.keys()
    sorted_project_sets = sorted(powerset(projects), key=map_project_set_to_cost, reverse=True)
    for ps in sorted_project_sets:
        print ("".join(sorted(ps)), ": ", map_project_set_to_cost(ps))



def proportional_budgeting(map_project_to_cost:dict, votes:list, limit:int)->set:
    """
    Implementation of the Aziz-Lee-Talmon algorithm for proportional budgeting.
    >>> map_project_to_cost = {"a":20, "b":15, "c":15, "d":10}
    >>> votes = ["ab", "ab", "ab", "ab", "c", "c"]
    >>> limit = 30
    >>> proportional_budgeting(map_project_to_cost, votes, limit)
    {'a'}
    """
    budgeted_projects = set()
    votes[:] = map(set, votes)   # convert every vote to a set
    num_of_voters = len(votes)
    money_per_voter = limit / num_of_voters
    logger.info("\nLimit={}. Voters={}. Money per voter={}".format(limit, len(votes),money_per_voter))
    for i in range(len(votes)):
        votes[i] = set(votes[i])
    map_project_set_to_cost = lambda ps: sum([map_project_to_cost[p] for p in ps])
    projects = map_project_to_cost.keys()
    sorted_project_sets = sorted(powerset(projects), key=map_project_set_to_cost, reverse=True)
    for ps in sorted_project_sets:
        supporting_votes = [vote for vote in votes if vote.issuperset(ps)]
        supporting_money = money_per_voter * len(supporting_votes)
        if map_project_set_to_cost(ps) <= supporting_money:
            logger.info("{}: cost {}, funded by {} voters!".format(
                "".join(sorted(ps)), map_project_set_to_cost(ps), len(supporting_votes)))
            budgeted_projects = budgeted_projects.union(ps)
            votes = [vote for vote in votes if not vote.issuperset(ps)]
        else:
            logger.info("{}: cost {}, supported by {} voters -- too expensive".format(
                "".join(sorted(ps)), map_project_set_to_cost(ps), len(supporting_votes)))
    return budgeted_projects


logger.setLevel(logging.INFO)
map_project_to_cost = {"a":20, "b":15, "c":15, "d":10}
votes = ["ab","ab","ab","ab","c","c"]
limit = 30
print(proportional_budgeting(map_project_to_cost, votes, limit))

map_project_to_cost = {"a":20, "b":20, "c":20}
votes = ["a","ab","bc","c"]
limit = 40
print(proportional_budgeting(map_project_to_cost, votes, limit))

