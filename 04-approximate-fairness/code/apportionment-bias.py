#!python3

"""
A demo of large/small party bias in apportionment methods.
"""

# from here: https://github.com/martinlackner/apportionment
import apportionment.methods as app

parties = ['A', 'B', 'C']
votes = [210,50,40]
seats = 3
app.compute("adams", votes, seats, parties, verbose=True)
app.compute("dean", votes, seats, parties, verbose=True)
app.compute("hill", votes, seats, parties, verbose=True)
app.compute("webster", votes, seats, parties, verbose=True)
app.compute("jefferson", votes, seats, parties, verbose=True)
