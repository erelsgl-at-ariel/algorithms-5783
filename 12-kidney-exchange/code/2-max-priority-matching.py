"""
Demonstrates maximum weight and maximum priority matching in python.
Programmer: Erel Segal-Halevi
Since: 2023-01
"""

import networkx as nx

def print_sorted_matching(matching:list):
    print(sorted([sorted(e) for e in matching]))


G=nx.Graph()

# Add edges without weights:
G.add_weighted_edges_from([
    ('a','b', 10), ('c','d', 6), ('a','c', 9), ('b','d', 8),
    ('e','f', 3), ('f','g', 2), ('g','e', 1),
    ('e','d', 4), ('d','h', 5), ('h','i', 7)
    ]
)

print("\nMax weight matching:")
print_sorted_matching(nx.max_weight_matching(G))

import networkx as nx
def max_priority_matching(G: nx.Graph):
    G = G.copy()
    map_edge_to_priority = {(u,v): data["weight"] for u,v,data in G.edges(data=True)}
    edges_sorted_by_priority = sorted(G.edges, key=map_edge_to_priority.__getitem__)
    print("edges_sorted_by_priority: ", edges_sorted_by_priority)
    map_edge_to_weight = {e: 2**i for i,e in enumerate(edges_sorted_by_priority)}
    print("map_edge_to_weight: ", map_edge_to_weight)
    for u,v,data in G.edges(data=True):
        data["weight"] = map_edge_to_weight[(u,v)]
    return nx.max_weight_matching(G)
    
print("\nMax priority matching:")
print_sorted_matching(max_priority_matching(G))
 