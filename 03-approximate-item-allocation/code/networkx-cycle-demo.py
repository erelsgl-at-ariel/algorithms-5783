#!python3

"""
A demo of finding a cycle using networkx -
the graph-algorithms package of python.
"""

import networkx as nx

def create_graph():
    """
    >>> G = create_graph()
    >>> list(G.edges(data=True))
    [('avi', 'beni', {'weight': 2}), ('beni', 'rami', {'weight': 3}), ('rami', 'avi', {'weight': 4})]
    """
    G = nx.DiGraph()

    # Add edges:
    G.add_edge('avi', 'beni', weight=2)
    G.add_edge('beni', 'rami', weight=3)
    G.add_edge('rami', 'avi', weight=4)
    return G

G = create_graph()

# Find cycles:
for cycle in nx.simple_cycles(G):
    print(cycle)
