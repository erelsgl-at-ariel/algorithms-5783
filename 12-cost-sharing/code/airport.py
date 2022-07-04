#!python3

"""
Calculate the Shapley values in the airport problem.

Programmer: Erel Segal-Halevi
Since: 2019-12
"""


import itertools, collections, powerset
from dicttools import stringify  # Install dicttools from here: https://github.com/trzemecki/dicttools

import logging
logger = logging.getLogger(__name__)


import shapley


def shapley_values_inefficient(map_player_to_cost:dict):
	"""
	Calculates the Shapley values for all players in an instance of the airport problem.
	NOTE: values are calculated inefficiently, by creating an instance of the generic Shapley value problem.
	This is done for demonstration purposes only.

	:param map_player_to_cost:  a dict where each key is a char representing a single player, and its value is the cost of that player (alone).
	:return: a dict where each key is a single char representing a player, and each value is the player's Shapley value.

	>>> stringify(shapley_values_inefficient({"a": 3}))
	'{a:3.0}'

	>>> stringify(shapley_values_inefficient({"a": 3, "b": 23}))
	'{a:1.5, b:21.5}'

	>>> stringify(shapley_values_inefficient({"a": 3, "b": 23, "c": 123}))
	'{a:1.0, b:11.0, c:111.0}'
	"""
	all_players = map_player_to_cost.keys()
	map_subset_to_cost = {
		"".join(sorted(subset)): max([map_player_to_cost[player] for player in subset])
		for subset in powerset.powerset(all_players)
		if len(subset)>0
	}
	map_subset_to_cost[""] = 0
	# print(map_subset_to_cost)
	return shapley.values(all_players, map_subset_to_cost)


if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
