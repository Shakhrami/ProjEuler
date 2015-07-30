#?/usr/bin/env python

#Prob 25: 1000-digit Fib number
import math
import time

# def fib(x):
#     if(x==1 or x==2):
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
#     
# for i in range(1000, 5000):
#     print "i=",i
#     fibString = str(fib(i))
#     if(len(fibString) == 1000):
#         print i
#         break

# def closed_form_fib(index):
#     phi = (1 + math.sqrt(5))/float(2)
#     psi = (1 - math.sqrt(5))/float(2)
#     
#     numerator = (math.pow(phi,index) - math.pow(psi, index))
#     denominator = math.sqrt(5)
#     return int(numerator/denominator)

"""
Faster fib method I found online that acutally runs
"""

def fibonacci(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a
    
t = time.time()
for i in range(2000, 50000):
    x = len(str(fibonacci(i)))
    if (x == 1000):
        print "index at:", i
        break
print time.time() - t, "seconds"