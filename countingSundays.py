#?/usr/bin/env python

#Prob 19: Counting Sundays

def days_per_month(month, year):
    if(month == 1):
        if((year % 4 == 0 and year % 100 != 0)or(year % 400 ==0)):
            return 29
        else:
            return 28
    if(month == 3 or month == 5 or month == 8 or month == 10):
        return 30
    else:
        return 31

dayOfWeek = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday",
             4:"Thursday", 5:"Friday", 6:"Saturday"}

weekday = 2 #Jan 1st 1901 is a tuesday
sunOnMon = 0

for year in range(1901, 2001):
    for month in range(0,12):
        daysThisMonth = days_per_month(month, year)
        
        for i in range(0, daysThisMonth):
            if(i == 0 and dayOfWeek[weekday] == "Sunday"):
                sunOnMon +=1
                #print"SunOnMon found at year", year, "month", month 
            weekday +=1
            if(weekday == 7):
                weekday = 0
print sunOnMon
