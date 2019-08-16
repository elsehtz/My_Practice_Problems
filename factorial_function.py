# Counts how many factorials of a number
def factorial(n, M): # n number, M mod this number, i.e n<M
    ans=1
    while(n>=1):
        ans=(ans*n)%M
        n-=1
    return ans


# >>Understanding of common data structures and when to use them 
#       - array/lists, maps/hashes, and sets
# >>JSON parsing and serialization
# >>The basics of HTTP requests - performing GET and POST requests,
#       understanding headers and status codes