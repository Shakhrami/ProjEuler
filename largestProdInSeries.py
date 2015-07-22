#?/usr/bin/env python

#def finds_zeros(series):
#    I want to come back to this and use this method somehow. 
#    return [i for i, num in enumerate(series) if num == '0']

#print finds_zeros(str(10111011111110))

def make_intList(number):
    return [int(n) for n in str(number)]

def max_sub_prod(series):
    largest_found = 0
    position = 0
    for i in range(1,len(series)):
        if(position == len(series) - 13):
                FinTest = (series[i-1] * series[(i)] * series[(i+1)] * series[(i+2)]*
                    series[(i+3)] * series[(i+4)] * series[(i+5)] * series[(i+6)]*
                    series[(i+7)]* series[(i+8)] * series[(i+9)] * series[(i+10)]*
                    series[(i+11)])
                if(FinTest > largest_found):
                    largest_found = FinTest
                return "largest found", largest_found
        else:
            test = (series[i-1] * series[(i)] * series[(i+1)] * series[(i+2)]*
                    series[(i+3)] * series[(i+4)] * series[(i+5)] * series[(i+6)]*
                    series[(i+7)]* series[(i+8)] * series[(i+9)] * series[(i+10)]*
                    series[(i+11)])
            #print "test=", test
            if(test > largest_found):
                #print "found a new larger = ", test
                largest_found = test
            position += 1
            
#awesome method to break up a really long integer.            
x = int("""
731671765313306249192251196744265747423553491949349698352031277450632623957831
801698480186947885184385861560789112949495459501737958331952853208805511125406
987471585238630507156932909632952274430435576689664895044524452316173185640309
871112172238311362229893423380308135336276614282806444486645238749303589072962
904915604407723907138105158593079608667017242712188399879790879227492190169972
088809377665727333001053367881220235421809751254540594752243525849077116705560
136048395864467063244157221553975369781797784617406495514929086256932197846862
248283972241375657056057490261407972968652414535100474821663704844031998900088
952434506585412275886668811642717147992444292823086346567481391912316282458617
866458359124566529476545682848912883142607690042242190226710556263211111093705
442175069416589604080719840385096245544436298123098787992724428490918884580156
166097919133875499200524063689912560717606058861164671094050775410022569831552
0005593572972571636269561882670428252483600823257530420752963450
""".replace("\n",""))


print max_sub_prod(make_intList(x))
