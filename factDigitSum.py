#?/usr/bin/env python

#Prob 20: Factorial Digit Sum
import math

num = str(math.factorial(100))
total = 0
for char in num:
    total += int(char)
    
print total
