#!python3

from  sympy import *
a,b,p = symbols('a b p')
x_lower_bound = 1/2 - (a-b)*(p-1/2)/(a+b+2*p)

ratio_a_lower_bound = (a+x_lower_bound)/(a+p)
print("Ratio for party a is larger than ", simplify(ratio_a_lower_bound))

ratio_b_upper_bound = (b+1-x_lower_bound)/(b+p)
print("Ratio for party b is smaller than ", simplify(ratio_b_upper_bound))

y_upper_bound = 1/2 - (b-a)*(p-1/2)/(a+b+2*p)
print("x+y = ",simplify(y_upper_bound+x_lower_bound))
