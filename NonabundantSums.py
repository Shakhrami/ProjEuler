#?/usr/bin/env python

#Prob 23: Non-abundant sums
import math

def proper_divisors(number):
    divisors = set()
    divisors.add(1)
    for i in range(2, int(math.sqrt(number))+1):
        if (number % i == 0):
            divisors.add(i)
            if(number/i not in divisors):
                divisors.add(number/i)
    return divisors

def all_Abundant_under(number):
    abundant = []
    for i in range(12, number):
        if(sum(proper_divisors(i)) > i):
            abundant.append(i)
    return abundant

abundants = all_Abundant_under(28124)


cant_be_expressed_sum = 0
sums = set()
for i in range(0, len(abundants)):
    for j in range(i, len(abundants)):
         summation = abundants[i] + abundants[j]
         if(summation not in sums):
             sums.add(summation)


for i in range(1, 28124):
    if i not in sums:
        #print i, "is not in sum"
        cant_be_expressed_sum += i
    #else:
        #print i, "can be represented as 2 abunds"

print cant_be_expressed_sum



