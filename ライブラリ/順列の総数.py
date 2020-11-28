import math as m
def permutation(n,r,m=1):
    a,b=0,0
    for i in range(n-r): a=(a*(i+1))%m
    for i in range(n): b=(b*(i+1))%m
    return b/a