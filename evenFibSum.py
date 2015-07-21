#?/usr/bin/env python
def fib(x):
    if(x==1 or x==2):
        return 1
    else:
        return fib(x-1) + fib(x-2)

total = 0
i=1
while True:
    if(fib(i) > 4000000):
        break
    if(fib(i) % 2 == 0):
        print("adding:"), fib(i)
        total += fib(i)
    i +=1

print("Sum of even fib's up to 4mil = "), total
