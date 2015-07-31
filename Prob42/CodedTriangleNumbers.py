#?/usr/bin/env python

#Prob 42: Coded Triangle Numbers

import csv

with open("words.txt") as csvfile:
    infile = csv.reader(csvfile)
    temp_list = list(infile)
    
word_list = temp_list[0]

letterNum = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,
             "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15,
             "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22,
             "W":23, "X":24, "Y":25, "Z":26}

score_of_each_word = []
for i in range(0, len(word_list)):
    word_score = 0
    for char in word_list[i]:
        word_score += letterNum[char]
    score_of_each_word.append(word_score)

#print max(score_of_each_word)
triangulars = set()
for i in range(0, 21):
    triangulars.add((i * (i + 1))/2)

total = 0
for score in score_of_each_word:
    if score in triangulars:
        total += 1
print total       