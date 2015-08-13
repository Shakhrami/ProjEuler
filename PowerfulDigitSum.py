#?/usr/beqin/env python

# Prob 56: Powerful digit sum

def digit_sum(number):
    digitSum = 0
    num = str(number)
    for char in num:
        digitSum += int(char)
    return digitSum


largestSum = 0

for a in range(2, 101):
    for b in range(1,101):
        test = digit_sum(int(a**b))
        if(test > largestSum):
            largestSum = test

print largestSum
        