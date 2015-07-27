#?/usr/bin/env python

#Prob 17: Number letter counts

def int_to_word(number):
    small = {0: "", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
             8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
             14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
             19:"nineteen"}
    
    tens = {2:"tewnty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy",
            8:"eighty", 9:"ninety"}
    
    hund = " hundred"
    
    if(number == 1000):
        return "one thousand"
    
    if(number < 100 and number > 19):
        last = small[number % 10]
        first = tens[int(str(number)[0])]
        return first +" "+last
    
    if(number >= 100):
        if(number % 100 == 0):
            return small[int(str(number)[0])] + hund
        
        first = small[int(str(number)[0])] + hund + " and "
        shorten = number % 100
        if(shorten > 19):
            shortenLast = small[shorten % 10]
            shortenFirst = tens[int(str(shorten)[0])]
            shortened = shortenFirst + " " + shortenLast
        else:
            shortened = small[shorten]
        return first + shortened
    else:
        return small[number]
    

def count_letters(word):
    count = 0
    for char in word:
        if(char != " "):
            count += 1
    return count

total = 0
for i in range(1, 1001):
    total += count_letters(int_to_word(i))

print total
