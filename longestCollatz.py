#?/usr/bin/env python

#Prob 14 Longest Collatz Sequence

import time
def len_of_Coll_Seq(number):
    if(number < 1):
        return 0
    
    count = 1
    while number != 1:
        if(number % 2 ==  0):
            number /= 2
        else:
            number = (3*number) + 1
        count += 1
    return count

t = time.time()
collLength = []
for i in range(0, 1000000):
    collLength.append(0)
    collLength[i] = len_of_Coll_Seq(i)



print collLength.index(max(collLength))
print time.time() - t, "seconds"