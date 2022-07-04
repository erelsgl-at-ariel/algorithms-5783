#!python3

"""
Calculate the Shapley value in the ride-sharing problem,
with a single pickup location and a fixed dropoff order.

Reference:

Chaya Levinger, Noam Hazon, Amos Azaria (2019)
[Fair Sharing: The Shapley Value for Ride-Sharing and Routing Games](https://arxiv.org/abs/1909.04713)


Programmer: Erel Segal-Halevi
Since: 2019-12
"""

import shapley

import powerset
from dicttools import stringify  # Install dicttools from here: https://github.com/trzemecki/dicttools

import logging
logger = logging.getLogger(__name__)



import networkx
from networkx import DiGraph


def path_cost(road_graph: DiGraph, path: list)->float:
	"""
	Calculate the total cost of the given path in the given graph.

	:param road_graph:  a weighted directed graph, representing travel costs between destinations.
	:param path: a list of destinations that must be traveled in the given order.
	:return the length of traveling the path in the given order.

	>>> road_graph = DiGraph()
	>>> road_graph.add_edge("0", "a", weight=11)
	>>> road_graph.add_edge("a", "b", weight=22)
	>>> road_graph.add_edge("b", "a", weight=44)
	>>> path_cost(road_graph, ["0","a","b"])
	33
	>>> path_cost(road_graph, ["0","b","a"])
	77
	"""
	length = 0
	for i in range(len(path)-1):
		length += networkx.dijkstra_path_length(road_graph, path[i], path[i+1])
	return length


def sublist(the_list:list, the_set:set)->list:
	"""
	return a sub-list of the_list, where the elements are from the_set.

	>>> sublist([1,2,3,4,5], set([5,3,1]))
	[1, 3, 5]

	>>> sublist([1,2,3,4,5], set([4,2,3]))
	[2, 3, 4]
	"""
	return list([item for item in the_list if item in the_set])



def shapley_values_inefficient(road_graph:DiGraph, path:list):
	"""
	Calculates the Shapley values for all players in an instance of the ride-sharing problem.
	NOTE: values are calculated inefficiently, by constructing an instance of the generic Shapley value problem.
	This is done for demonstration purposes only.

	:param road_graph:  a weighted directed graph, representing travel costs between destinations.
	:param path: the first element is the source; then comes the list of passangers, in the fixed order by which they should be dropped from the taxi.
	:return: a dict where each key is a single char representing a passanger, and each value is the player's Shapley value.

	>>> road_graph = DiGraph()
	>>> road_graph.add_edge("0", "a", weight=5)
	>>> road_graph.add_edge("0", "b", weight=9)
	>>> road_graph.add_edge("a", "b", weight=6)
	>>> road_graph.add_edge("b", "a", weight=6)
	>>> stringify(shapley_values_inefficient(road_graph, ["0", "a", "b"]))
	'{a:3.5, b:7.5}'

	>>> stringify(shapley_values_inefficient(road_graph, ["0", "b", "a"]))
	'{a:5.5, b:9.5}'
	"""
	source = path[0]
	players = path[1:]
	map_subset_to_cost = {
		"".join(sorted(subset)): path_cost(road_graph, [source]+sublist(players, subset))
		for subset in powerset.powerset(players)
		if len(subset)>0
	}
	map_subset_to_cost[""] = 0
	return shapley.values("".join(players), map_subset_to_cost)


def shapley_values_efficient(road_graph:DiGraph, path:list):
	"""
	Calculates the Shapley values for all players in an instance of the ride-sharing problem.
	Uses an efficient calculation, based on Levinger, Hazon, and Azaria (2019)

	:param road_graph:  a weighted directed graph, representing travel costs between destinations.
	                    "0" denotes the source; all other nodes are destinations.
	:param path: the first element is the source; then comes the list of passangers, in the fixed order by which they should be dropped from the taxi.
	:return: a dict where each key is a single char representing a passanger, and each value is the player's Shapley value.

	>>> road_graph = DiGraph()
	>>> road_graph.add_edge("0", "a", weight=5)
	>>> road_graph.add_edge("0", "b", weight=9)
	>>> road_graph.add_edge("a", "b", weight=6)
	>>> road_graph.add_edge("b", "a", weight=6)
	>>> stringify(shapley_values_efficient(road_graph, ["0", "a", "b"]))
	'{a:3.5, b:7.5}'

	>>> stringify(shapley_values_efficient(road_graph, ["0", "b", "a"]))
	'{a:5.5, b:9.5}'
	"""
	source = path[0]
	# NOTE: player index starts at 1. Source is 0.
	map_player_to_value = {player:0.0 for player in path[1:]}

	for k in range(1, len(path)):  # NOTE: player index starts at 1. Source is 0.
		d_0_k = networkx.dijkstra_path_length(road_graph, source, path[k])
		logger.info("Calculate Shapley-values for sub-problem with only d[0,%d] (= %f):", k, d_0_k)
		logger.info("  Player %d adds d[0,%d] whenever he is first among 1,...,%d, which happens in 1/%d of the orders.", k, k, k, k)
		map_player_to_value[path[k]] += d_0_k / k  # player k adds d_0_k whenever he is first among 1,...,k, which happens in 1/k of the orders.
		for j in range(1, k):                          # each player j<k removes d_0_k whenever he is first among 1,...,k-1 that comes after k.
			logger.info("  Player %d removes d[0,%d] whenever he is first among 1,...,%d-1 that comes after %d.", j, k, k, k)
			map_player_to_value[path[j]] -= d_0_k / k / (k-1)  # This happens in 1/k(k-1) of the orders.

		for i in range(1, k):
			d_i_k = networkx.dijkstra_path_length(road_graph, path[i], path[k])
			logger.info("Calculate Shapley-values for sub-problem with only d[%d,%d] (= %f):", i, k, d_i_k)
			logger.info("  Player %d adds d[%d,%d] whenever %d is second and %d is first among %d,...,%d, which happens in 1/(%d-%d+1)/(%d-%d) of the orders.", i, i,k, i,k, i,k, k,i, k,i)
			map_player_to_value[path[i]] += d_i_k / (k-i+1) / (k-i)
			map_player_to_value[path[k]] += d_i_k / (k-i+1) / (k-i)
			for j in range(i+1, k):                         # each player j with i<j<k removes d_i_k whenever he is first among i+1,...,k-1 that comes after i,k.
				map_player_to_value[path[j]] -= d_i_k / (k-i+1) / (k-i) / (k-i-1) * 2
	return map_player_to_value


if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
