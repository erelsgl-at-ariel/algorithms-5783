#!python3

import itertools
import collections

import logging
logger = logging.getLogger(__name__)

import logging, sys
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


def shapley_values(num_of_players:int, map_subset_to_cost:dict):
	"""
	Calculate the Shapley values for all players.
	:param num_of_players: Total number of players.
	:param map_subset_to_cost:  a dict where each key is a subset of the players, and its value is the cost of that subset.
	:return: a dict where each key is a single player and each value is the player's Shapley value.
	"""

	map_player_to_sum_of_marginal_costs = collections.defaultdict(float)
	num_permutations = 0
	all_players = range(1,num_of_players+1)
	logger.info("Looping over all permutations of %s", list(all_players))
	for permutation in itertools.permutations(all_players):
		# calculate marginal costs for a specific permutation:
		logger.info("  Permutation %s: ", permutation)
		current_cost = 0
		current_subset = set()
		for player in permutation:	# loop over the players in the order given by the current permutation
			# calculate marginal cost for a specific player in a specific permutation
			current_subset.add(player)
			new_cost = map_subset_to_cost[frozenset(current_subset)]
			marginal_cost = new_cost - current_cost
			logger.info("    Player %s: %d", player, marginal_cost)
			map_player_to_sum_of_marginal_costs[player] += marginal_cost
			current_cost = new_cost
		num_permutations += 1

	for player,cost in map_player_to_sum_of_marginal_costs.items():
		map_player_to_sum_of_marginal_costs[player] = cost/num_permutations

	return map_player_to_sum_of_marginal_costs

if __name__=="__main__":
	map_subset_to_cost = {
		frozenset():		0,
		frozenset({1}):	 1000,
		frozenset({2}):	 2000,
		frozenset({1,2}):   2000,
		frozenset({3}):	 3000,
		frozenset({1,3}):   3000,
		frozenset({2,3}):   3000,
		frozenset({1,2,3}): 3000,
	}
	sv = shapley_values(3, map_subset_to_cost)
	print("Shapley values: ", sv, flush=True)


