#?/usr/bin/env python

import time
def sum_up_to_n(n):
    return (n*(n+1))/2

def sum_of_squares(n):
    return (n*(n+1)*(2*n + 1))/6

t= time.time()
x=  sum_up_to_n(100)
y= sum_of_squares(100)
print x**2 - y
print time.time()-t, "seconds"
