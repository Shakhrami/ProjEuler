#?/usr/bin/env python

#Prob 9: Special Pythagorean triplet

for i in range(1, 100, 2):
   for j in range(3, 100, 2):
        r = i
        s = j
    
        a = r*s
        b = ((s*s)-(r*r))/2
        c = ((s*s)+(r*r))/2
        
        #print "--------------"
        #print "**i=", i, "a=", a, "b=", b, "c=", c
        #print "--------------"
            
        if((a+b+c)  == 1000):
            print "a= ", a
            print "b= ", b
            print "c= ", c
            print "a*b*c = ", a*b*c

