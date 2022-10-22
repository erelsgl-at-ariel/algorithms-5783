#!python3

"""
Demo of Shapley value calculation.

Programmer: Erel Segal-Halevi
Since: 2019-12
"""

import shapley, logging, sys
shapley.logger.addHandler(logging.StreamHandler(sys.stdout))
shapley.logger.setLevel(logging.INFO)


print("\n## Ride-sharing example")
map_subset_to_cost = {
	"":	   0,
	"a":   5,
	"b":   9,
	"ab":  11,
}
shapley.show(shapley.values("ab", map_subset_to_cost))


print("\n## Airport problem example")
map_subset_to_cost = {
	"":	   0,
	"a":   3,
	"b":   23,
	"c":   123,
	"ab":  23,
	"ac":  123,
	"bc":  123,
	"abc": 123,
}
shapley.show(shapley.values("abc", map_subset_to_cost))

