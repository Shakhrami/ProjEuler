#?/usr/bin/env python

#Prob 21: Amicable Numbers

def proper_divisors(number):
    divisors = []
    for i in range(1, number):
        if (number % i == 0):
            divisors.append(i)
    return divisors

def find_amic_up_to(number):
    amic = []
    for i in range(2,number+1):
        x = sum(proper_divisors(i))
        if(sum(proper_divisors(x)) == i and x !=i):
            amic.append(i)
    return amic

x = find_amic_up_to(10000)
print x
print "Sum = ", sum(x)