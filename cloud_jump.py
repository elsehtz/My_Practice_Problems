
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n_jumps=0
    idx = 0
    while idx<len(c):
        if(idx+1==len(c)):  
            return n_jumps
        elif(idx+2==len(c)):
            return n_jumps+1
        elif(c[idx+2]==0):
            idx+=2
        else:
            idx+=1
        n_jumps+=1
    return n_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
