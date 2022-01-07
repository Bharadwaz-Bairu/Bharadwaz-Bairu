'''
logic : 
julian calender :
        in 1918 there are only 15 days in feb
        before 1918
            every year divisible by 4 is a leap year 
        after 1918 
            if year divisible by 4 , 100 and 400 is leap year 
            if year divisible by 4 is a leap year 
            if year divisible by 4 and 100 but not 400 is not a leap year 

'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def isleapYear(year):
    if year > 1918:
        if ((year%4 == 0 and year%100 !=0) or (year%4==0 and year%400 == 0)):
            return True
        else : 
            return False
        
    elif year < 1918 and year %4 ==0  :
        return True 
    else :
        return False 
def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26.09.1918"
    else:
        if isleapYear(year):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
