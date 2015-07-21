#?/usr/bin/env python

largest = 0
def factors(x):
    global largest
    for i in range(2, int(x**0.5)+1):
        if(x % i == 0):
            #print("Factor found:"), i
            if(is_prime(i)):
                if(i > largest):
                    largest = i
                

def is_prime(y):
    #print("counting up to "), y
    if(y == 2):
        return True
    for i in range(3, int(y**0.5)+1, 2):
        if(y % i == 0):
            #print i, "divides ", y
            return False
    return True
            
#factors(13195)
factors(600851475143)
print("largest = "), largest