N=int(input())
B=list(map(int,input().split()))
A=[0]*N
for i in range(N):
    if i==0: A[i]=B[i]
    elif i<N-1: A[i]=min(B[i-1],B[i])
    else: A[i]=B[i-1]
print(sum(A))