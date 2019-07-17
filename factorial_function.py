def factorial(n, M): # n number, M mod this number, i.e n<M
    ans=1
    while(n>=1):
        ans=(ans*n)%M
        n-=1
    return ans