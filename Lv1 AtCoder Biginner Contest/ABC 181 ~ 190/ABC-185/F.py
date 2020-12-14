N,Q=map(int,input().split())
A=map(int,input().split())

for i in range(Q):
    T,X,Y=map(int,input().split())
    if T==1:
        A[X-1]=A[X-1]^A[Y-1]
    else: