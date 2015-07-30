#?/usr/bin/env python

#Prob 29: Distinct powers
import math

products = set()
for a in range(2,101):
    for b in range(2,101):
        x = math.pow(a,b)
        if(x not in products):
            products.add(x)

print len(products)