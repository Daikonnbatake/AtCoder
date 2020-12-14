import math
def c(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

L=int(input())-11
ans=0
