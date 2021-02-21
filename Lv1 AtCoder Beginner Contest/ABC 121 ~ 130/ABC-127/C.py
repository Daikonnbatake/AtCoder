N,M=map(int,input().split())
ans=0
L,R=0,(10**5)+1
for i in range(M):
    l,r=map(int,input().split())
    L=max(L,l); R=min(R,r)
    if r<l: break
R=min(R,N)
print(abs((L-1)-R) if 0<=R-L else 0)