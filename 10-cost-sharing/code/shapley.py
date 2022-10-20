#!python3

"""
Shapley value calculation.

Programmer: Erel Segal-Halevi
Since: 2019-12
"""


import itertools, collections
from dicttools import stringify  # Install dicttools from here: https://github.com/trzemecki/dicttools

import logging
logger = logging.getLogger(__name__)


def values(all_players:str, map_subset_to_cost:dict):
	"""
	Calculate the Shapley values for all players.
	:param all_players: a string where each char represents a player.
	:param map_subset_to_cost:  a dict where each key is a string representing a subset of players, and its value is the cost of that subset.
	:return: a dict where each key is a single char representing a player, and each value is the player's Shapley value.

	>>> stringify(values("a", {"": 0, "a": 10}))
	'{a:10.0}'
	>>> stringify(values("ab", {"": 0, "a": 10, "b": 0, "ab": 10}))
	'{a:10.0, b:0.0}'
	>>> stringify(values("ab", {"": 0, "a": 10, "b": 5, "ab": 15}))
	'{a:10.0, b:5.0}'
	>>> stringify(values("ab", {"": 0, "a": 10, "b": 5, "ab": 10}))
	'{a:7.5, b:2.5}'
	"""

	map_player_to_sum_of_marginal_costs = collections.defaultdict(float)
	num_permutations = 0
	logger.info("Looping over all permutations of %s", list(all_players))
	for permutation in itertools.permutations(all_players):
		# calculate marginal costs for a specific permutation:
		logger.info("  Permutation %s: ", permutation)
		current_cost = 0
		current_subset = ""
		for player in permutation:	# loop over the players in the order given by the current permutation
			# calculate marginal cost for a specific player in a specific permutation
			current_subset += player
			new_cost = map_subset_to_cost[''.join(sorted(current_subset))]
			marginal_cost = new_cost - current_cost
			logger.info("    Player %s: %d", player, marginal_cost)
			map_player_to_sum_of_marginal_costs[player] += marginal_cost
			current_cost = new_cost
		num_permutations += 1

	for player,cost in map_player_to_sum_of_marginal_costs.items():
		map_player_to_sum_of_marginal_costs[player] = cost/num_permutations

	return map_player_to_sum_of_marginal_costs


def show(map_player_to_shapley_value):
	"""
	Print the Shapley values to screen.
	"""
	for player,value in map_player_to_shapley_value.items():
		print("Shapley value of {} is {}".format(player, value))


if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
