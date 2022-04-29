import math
import os
import random
import re
import sys

#
# Complete the 'helpArman' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def helpArman(arr, brr):

    d = {}
    dd = {}
    a = []
    for i in brr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in arr:
        if i not in dd:
            dd[i] = 1
        else:
            dd[i] += 1
    

    for i in d.keys():
        if d[i] > dd[i]:
            a.append(i)
    return sorted(a)
            
    
        

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
print(*helpArman(arr, brr))
# helpArman(arr, brr)
