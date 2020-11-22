N,Q=map(int,input().split())
a=[0]*N
for i in range(Q):
    L,R,T=map(int,input().split())
    for j in range(R-L+1):a[j+L-1]=T
for i in a:print(i)