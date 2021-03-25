N=int(input())
A=list(map(int,input().split()))
dp=[float('inf')*-1]*N
dp[0]=0

for i in range(1,N):
    a=A[i-1]+A[i]
    b=(A[i-1]*-1)+(A[i]*-1)
    if a<b:
        A[i-1]*=-1
        A[i]*=-1
    dp[i]=dp[i-1]+max(a,b)

print(dp)