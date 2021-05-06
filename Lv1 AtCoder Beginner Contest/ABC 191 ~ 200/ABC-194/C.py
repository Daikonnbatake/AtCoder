from collections import Counter as c
N=int(input())
A=map(int,input().split())
C=c()
ans=0
for a in A:
    for k,v in C.items():
        ans += v*((k-a)**2)
    C[a]+=1
print(ans)