import math
import os
import random
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar): # n = size of array; ar = array; find matches in array
    pairs = 0
    restart = 1
    print(arr)
    while restart:
        restart=0
        for i, val_1 in enumerate(ar):
            for j, val_2 in enumerate(ar):
                if((val_1==val_2) and (i != j)):
                    del ar[j]
                    del ar[i]
                    pairs+=1
                    restart=1
                    break
            if(restart):
                break
        
    print(ar)
    return pairs

if __name__ == '__main__':
    arr = [50, 50, 10, 20]
    print(sockMerchant(len(arr),arr))
    