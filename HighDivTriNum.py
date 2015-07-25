#?/usr/bin/env python

#Prob 12: Highly divisible triangular number

import math

def triangular(num):
    """ Returns the nth triangular number """
    return (num * (num+1))/2

def num_of_factors(num):
    numOfFactors = 1
    for i in range(2, int(math.sqrt(num)) + 1):
       #print "checking if", i, " divides", num
        if(num % i == 0):
            numOfFactors += 1
    
    return numOfFactors*2
    
    
found = False
index = 10
while found != True:
    if(num_of_factors(triangular(index)) > 500):
        print triangular(index)
        found = True
    index +=1
    