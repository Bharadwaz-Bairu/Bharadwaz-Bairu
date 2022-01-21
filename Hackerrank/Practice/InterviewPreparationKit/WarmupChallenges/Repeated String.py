#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    sl = len(s)
    if 'a' not in s:
        return 0
    if len(list(set(s))) == 1 and s[0]=='a':
        return n
    acount = 0
    for i in range(sl):
        if s[i] == 'a':
            acount +=1
    length = math.floor(n/sl) 
    value = length*acount
    if n/sl != 0 :
        for i in range(n%sl):
            if s[i] == 'a':
                value+=1
    return value
                
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
