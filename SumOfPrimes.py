#?/usr/bin/env python
#Prob 10 Summation of primes


#Pretty slow, but it works. Want to come back to this.
import math, time

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    
    return True

def primes_below(number):
    primes = []
    for i in range(2, number+1):
        if(is_prime(i)):
            primes.append(i)
    return primes

t= time.time()
z = 2000000
print "Sum = ", sum(primes_below(z))
print time.time() - t