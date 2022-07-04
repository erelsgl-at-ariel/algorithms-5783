#!python3

import networkx as nx

G=nx.Graph()

# Add edges with weights:
G.add_edge('a','b' ,weight=2)
G.add_edge('b','c',weight=3)
G.add_edge('c','d' ,weight=4)
#G.add_edge('d','e' ,weight=5)
#G.add_edge('e','a' ,weight=6)

print(nx.max_weight_matching(G))

