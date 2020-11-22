N,K=map(int,input().split())
#d=[list(map(int,input().split()))for i in range(K)]
a=[0]*(N+2)
for i in range(K):
    l,r=map(int,input().split())
    if l==r:a[l]+=1;a[l+1]-=1
    else:a[l]+=1;a[r+1]-=1
m,f=0,0
for i in range(1,N+1):
    if a[i]==1:f=1
    if a[i]==-1:f=0
    if f:m+=1
    a[i]=m
