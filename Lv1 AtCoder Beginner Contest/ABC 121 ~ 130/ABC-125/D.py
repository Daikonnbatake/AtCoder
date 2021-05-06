N=int(input())
A=list(map(int,input().split()))
dp=[0]*N

for i in range(1,N):
    a=dp[i-1]+A[i-1]+A[i]
    b=dp[i-1]+(A[i-1]*(-2 if 1<i else -1))+(A[i]*-1)
    dp[i]=max(a,b)
    if a<b:A[i-1]*=-1;A[i]*=-1

print(sum(A))