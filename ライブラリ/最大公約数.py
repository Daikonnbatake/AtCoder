import math
def agcd(l):
    if 1<len(l):
        a=math.gcd(l[0],l[1])
        for i in range(2,len(l)):
            a=math.gcd(a,l[i])
    else:a=l[0]
    return a