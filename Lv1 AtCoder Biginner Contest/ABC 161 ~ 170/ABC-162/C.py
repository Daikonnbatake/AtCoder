import math
from functools import reduce
K = int(input())

def gcd(l):
    return reduce(math.gcd, l)
count = 0
for a in range(K):
    for b in range(K):
        for c in range(K):
            if a+1 == 1 or b+1 == 1 or c+1 == 1:
                count +=1
                pass
            else:
                count += gcd([a+1,b+1,c+1])
print(count)