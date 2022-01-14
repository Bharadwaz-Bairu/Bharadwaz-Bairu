#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#
'''
0|1     2|3     4|5   5|6
  |     |               |
  1 to 2 is less distance so distance between them 

Sample Input 0

6
2
Sample Output 0
1



Sample Input 1

5
4
Sample Output 1

0
'''

def pageCount(n, p):
    # Write your code here
    pa = (p//2) 
    if n//2 - pa < pa :
        pa = n//2 - pa
    
    return pa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
