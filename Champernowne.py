#?/usr/beqin/env python

# Prob 40: Champernowne's constant

champ =""
for i in range(1,1000001):
    champ += str(i)


x = int(champ[1 - 1]) * int(champ[10 -1]) * int(champ[100 - 1]) *\
    int(champ[1000 - 1]) * int(champ[10000 - 1]) * int(champ[100000 - 1]) *\
    int(champ[1000000 - 1])
print x 