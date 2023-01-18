"""
Demonstrates maximum matching in python.
Programmer: Erel Segal-Halevi
Since: 2023-01
"""

import networkx as nx

def print_sorted_matching(matching:list):
    print(sorted([sorted(e) for e in matching]))


G=nx.Graph()

# Add edges without weights:
G.add_edges_from([
    ('a','b'), ('a','c'), ('c','d'), ('b','d'),
    ('e','f'), ('f','g'), ('g','e'),
    ('e','d'), ('d','h'), ('h','i')
    ]
)
print_sorted_matching(nx.max_weight_matching(G))

