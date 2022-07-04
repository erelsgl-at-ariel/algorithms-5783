#!python3

"""
A demo of apportionment methods.
"""

# from here: https://github.com/martinlackner/apportionment
import apportionment.methods as app

def check_consistency(votes, seats, parties, methods):
    for method in methods:
        result = app.compute(method, votes, seats, parties)
        app.compute(method, [votes[0], votes[1]], result[0]+result[1], [parties[0], parties[1]])
        app.compute(method, [votes[0], votes[2]], result[0]+result[2], [parties[0], parties[2]])
        app.compute(method, [votes[1], votes[2]], result[1]+result[2], [parties[1], parties[2]])



# check_consistency([40, 135, 325], 5, ['A', 'B', 'C'], ["hamilton", "jefferson", "webster"])
check_consistency([25, 140, 335], 5, ['A', 'B', 'C'], ["hamilton", "jefferson", "webster"])
