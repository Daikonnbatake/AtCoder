import math
N=int(input())
s=set()
for i in range(2,10**5+1):
    if math.sqrt(N)<i:break
    m=i
    for j in range(1000):
        m*=i
        if N<m:break
        s.add(m)

print(N-len(s))