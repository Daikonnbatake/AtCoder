N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

A=[0]*(N+1)

for i in range(1,N+1):
    if a[A[i-1]] < a[i-1]:A[i]=i-1
    else: A[i] = A[i-1]

MAX=0
MAXB=0

for i in range(1,N+1):
    MAX = max(a[A[i]]*b[i-1],MAX)
    print(MAX)