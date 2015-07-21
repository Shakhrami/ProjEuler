#?/usr/bin/env python

def palindrome():
    palindrome = 0
    
    for i in range(100, 1000):
        for j in range(100, 1000):
            x = i*j
            #String reverse method
            str_x = str(x)
            rev_x = str_x[::-1]
            if(str_x == rev_x):
                if(x>palindrome):
                    palindrome = x
                    print palindrome, "<<<<<------"
                    

palindrome()