#?/usr/bin/env python

# Prob 28 : Number spiral diagonals

counterTotal = 1
jump = 2
count = 0
lastValue = 1

while jump <= (1000):
    value = lastValue + jump
    counterTotal += value
    #print "added", value
    lastValue = value
    count += 1
    if(count == 4):
        jump += 2
        count = 0

print counterTotal