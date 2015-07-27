#?/usr/bin/env python

#Prob 16: Power digit sum

import math
def sum_of_digits(number):
    total = 0
    for char in number:
        total += int(char)
    return total

number = int(math.pow(2,1000))
strNum= str(number)
print sum_of_digits(strNum)