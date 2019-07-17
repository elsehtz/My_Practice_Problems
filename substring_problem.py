# Sam Substring problem
from itertools import combinations 
# Complete the substrings function below.

def substrings(num):
    ans = int(num[0])
    previous_sum = int(num[0])
    mod = (10**9+7)
    for i in range(1,len(num)):
        # current sum = nth element * n + previous sum * 10         
        ans += (((int(num[i])*(i+1)) % mod) + ((previous_sum*10) % mod)) % mod
        previous_sum = (((int(num[i])*(i+1)) % mod) + ((previous_sum*10) % mod)) % mod
        
    return ans % mod

if __name__ == '__main__':
    num = '111'
    print(substrings(num))
    print(2*10**5)