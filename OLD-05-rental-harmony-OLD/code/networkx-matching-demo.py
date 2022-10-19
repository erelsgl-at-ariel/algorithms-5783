#!python3

"""
A demo of finding a matching in networkx -
the graph-algorithms package of python.
"""

import networkx as nx

# Create an unweighted graph:
G = nx.complete_bipartite_graph(2, 3)
left, right = nx.bipartite.sets(G)
print(list(left))   # [0, 1]
print(list(right))  # [2, 3, 4]
# Find a maximum cardinality matching:
print(nx.bipartite.maximum_matching(G)) # {0: 2, 1: 3, 2: 0, 3: 1}

# Add weights:
for u, v in G.edges(): G[u][v]["weight"] = 10*u+10+v
# Find a maximum weight matching:
print(nx.max_weight_matching(G))

# Change weights:
for u, v in G.edges(): G[u][v]["weight"] = 10*u+10-v
# Find another maximum weight matching:
print(nx.max_weight_matching(G))

