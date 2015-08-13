#?/usr/beqin/env python

# Prob 53

import math
def n_choose_r(n,r):
    numerator = math.factorial(n)
    denom = math.factorial(r)*(math.factorial(n-r))
    return numerator/denom

greaterThatOneMillion = 0

for n in range(1, 101):
    for r in range(1, n+1):
        if(n_choose_r(n,r) > 1000000):
            greaterThatOneMillion += 1

print greaterThatOneMillion