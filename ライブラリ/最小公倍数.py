import math
def lcm(l):
    if 1<len(l):
        r=l.pop(0)
        for i in l:
            r=r*i//math.gcd(r,i)
    else:r=l[0]
    return r