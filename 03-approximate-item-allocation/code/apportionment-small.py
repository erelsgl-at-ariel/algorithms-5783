#!python3

"""
A demo of large/small party bias in apportionment methods.
"""

# from here: https://github.com/martinlackner/apportionment
import apportionment.methods as app

def webster(total_seats: int, votes: list[int]) -> list[int]: 
	numparties = len(votes)
	seats = [0 for i in range(numparties)]  # איתחול
	for i in range(total_seats):     # מתן המושב הבא
		quotients = [votes[i]/(seats[i]+1/2) 
                     for i in range(numparties)]
		nextparty = max(range(numparties), key=lambda i:quotients[i])
		seats[nextparty] += 1
	return seats


parties = ['A', 'B', 'C']
votes = [1001,1002,1999]
seats = 120
app.compute("webster", votes, seats, parties, verbose=True)
print(webster(seats, votes))

