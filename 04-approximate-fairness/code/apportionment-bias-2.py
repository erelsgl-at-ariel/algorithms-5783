#!python3

"""
A demo of large/small party bias in apportionment methods.
"""

import apportionment.methods as app

a = 19
x = 0.1
b = 7
y = 1-x
p = 0.5

print((a+x)/(a-1+p) > (b+y)/(b+p))

votes = [int(1000*(a+x)), int(1000*(b+y))]
seats = a+b+1
parties = ["A", "B"]
app.compute("webster", votes, seats, parties, verbose=True)

