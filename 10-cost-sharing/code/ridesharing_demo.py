#!python3

"""
Demo of Shapley value calculation in the ride-sharing problem.

Programmer: Erel Segal-Halevi
Since: 2019-12
"""

from networkx import DiGraph


import ridesharing, logging, sys
ridesharing.logger.addHandler(logging.StreamHandler(sys.stdout))
ridesharing.logger.setLevel(logging.INFO)

import shapley
shapley.logger.addHandler(logging.StreamHandler(sys.stdout))
shapley.logger.setLevel(logging.INFO)

print("\n## Ride-sharing example - 2 travelers")
road_graph = DiGraph()
road_graph.add_edge("0", "a", weight=5)
road_graph.add_edge("0", "b", weight=9)
road_graph.add_edge("a", "b", weight=6)
print("\n#### Inefficient calculation")
shapley.show(ridesharing.shapley_values_inefficient(road_graph, ["0", "a", "b"]))

print("\n#### Efficient calculation")
shapley.show(ridesharing.shapley_values_efficient(road_graph, ["0", "a", "b"]))

print("\n## Ride-sharing example - 3 travelers")
road_graph = DiGraph()
road_graph.add_edge("0", "a", weight=10)
road_graph.add_edge("0", "b", weight=15)
road_graph.add_edge("0", "c", weight=25)
road_graph.add_edge("a", "b", weight=10)
road_graph.add_edge("a", "c", weight=15)
road_graph.add_edge("b", "c", weight=15)
print("\n#### Inefficient calculation")
shapley.show(ridesharing.shapley_values_inefficient(road_graph, ["0", "a", "b", "c"]))

print("\n#### Efficient calculation")
shapley.show(ridesharing.shapley_values_efficient(road_graph, ["0", "a", "b", "c"]))
