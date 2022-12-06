#!python3

"""
Using networkx - the graph algorithms package of Python -
to find a room assignment maximizing the sum of values.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import networkx as nx


print("\n\nThere are three tennants and three rooms.")

# Construct an empty graph:
G=nx.Graph()

# Add edges with weights:
G.add_edge('aya','martef' ,weight=2)
G.add_edge('aya','heder',weight=40)
G.add_edge('aya','salon' ,weight=35)

G.add_edge('batya','martef' ,weight=40)
G.add_edge('batya','heder',weight=3)
G.add_edge('batya','salon' ,weight=35)

G.add_edge('gila','martef' ,weight=20)
G.add_edge('gila','heder',weight=40)
G.add_edge('gila','salon' ,weight=4)

print("Maximum-value matching: ", nx.max_weight_matching(G))

