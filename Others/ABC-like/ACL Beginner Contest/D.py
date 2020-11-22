N,K=map(int,input().split())
A=[int(input())for i in range(N)]
a=sorted(A)
m=[a[N//2]] if N%2 else [a[N//2-1],a[N//2]]
ans=0
mem=0
if len(m)==2:
    for i in range(N):
        if abs(A[i]-m[1])<=K:mem+=1
for i in range(N):
    if abs(A[i]-m[0])<=K:ans+=1