#?/usr/bin/env python

import math
# Finds the nth prime number
def nthPrime(n):
    count = 0
    index = 2
    while count < n:
        if(is_prime(index)):
            count += 1
        index +=1
    
    print index -1
        
def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    
    return True
            


nthPrime(10001)