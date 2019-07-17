import math
import os
import random
import re
import sys

# Complete the countingValleys function below.

def countingValleys(n, s):
    elevation=0
    n_vallies=0
    move_list=list(s)
    valley_started = False
    for move in move_list:        
        
        if(move == 'U'):
            elevation+=1
        else:
            elevation-=1
        
        
        
        if(elevation<0):
            valley_started = True
        if(elevation>=0 and valley_started):
            n_vallies+=1
            valley_started = False

                
    return n_vallies
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
