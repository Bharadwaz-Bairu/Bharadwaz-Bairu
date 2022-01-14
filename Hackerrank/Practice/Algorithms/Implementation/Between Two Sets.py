#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def LCM(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    print(lcm,"lcm")
    return lcm
    
    
def HCF(arr):
    GCD = arr[0]
    for i in range(1,len(arr)):
        GCD = math.gcd(GCD,arr[i])
    return GCD
        
    

def getTotalX(a, b):
    # Write your code here
    lcm = LCM(a)
    hcf = HCF(b)
    i = 1
    arr = []
    while lcm*i <= hcf :
        if hcf%(i*lcm) == 0 :
            arr.append(lcm*i)
        i += 1
    return len(arr)
        
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
