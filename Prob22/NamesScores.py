#?/usr/bin/env python

import csv

#Prob 22: Names Scores
with open("names.txt") as csvfile:
    infile = csv.reader(csvfile)
    names_list = list(infile)

new_list = names_list[0]
new_list.sort()


letterNum = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,
             "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15,
             "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22,
             "W":23, "X":24, "Y":25, "Z":26}

total = 0
word_total = 0
for i in range(0, len(new_list)):
    for char in new_list[i]:
        word_total += letterNum[char]
    word_total *= (i + 1)
    total += word_total
    word_total = 0

print total
    
    
    