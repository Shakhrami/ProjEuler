#?/usr/bin/env python

import time

def smallest_mult_1_to_20():
    i=2
    while True:
        if(i%3 == 0 and i%4 == 0 and i%5 == 0 and i%6 == 0 and i%7 == 0 and
           i%8 == 0 and i%9 == 0 and i%10 == 0 and i%11 == 0 and i%12 == 0 and
           i%13 == 0 and i%14 == 0 and i%15 == 0 and i%16 == 0 and i%17 == 0 and
           i%18 == 0 and i%19 == 0 and i%20 == 0):
            print i
            return
        i+=2
        
t = time.time()    
smallest_mult_1_to_20()
print(time.time() - t), "seconds"

#want to update this. I'm sure it can be done faster.