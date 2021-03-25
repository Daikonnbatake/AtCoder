N=int(input())
dp=[0]*(N+1)

for i in range(1,N+1):
    dp[i]=10**5
    p=1
    while p<=i:
        dp[i]=min(dp[i],dp[i-p]+1)
        p*=6
    p=1
    while p<=i:
        dp[i]=min(dp[i],dp[i-p]+1)
        p*=9

print(dp[-1])