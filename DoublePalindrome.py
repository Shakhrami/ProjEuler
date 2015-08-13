#?/usr/beqin/env python

# Prob 36: Double-base palindromes

def to_base_10(number,givenBase):
    strBase = str(number)
    base10 = 0
    for i in range(0, len(strBase)):
        base10 += int(strBase[i])*math.pow(givenBase,len(strBase) - (i+1))
    return int(base10)

def to_base_q(base10, baseQ):
    x = base10
    str_forward = ""
    while x != 0:
        str_append = str(x % baseQ)
        str_forward += str_append
        x = (x - int(str_append))/baseQ
        
    return int(str_forward[::-1])

def is_palindrome(number):
    str_num = str(number)
    rev_num = str_num[::-1]
    if(str_num == rev_num):
        return True
    return False

both = []
for i in range(1, 1000000):
    i_base2 = to_base_q(i, 2)
    if(is_palindrome(i) and is_palindrome(i_base2)):
        both.append(i)

print both
print "Sum = ", sum(both)
