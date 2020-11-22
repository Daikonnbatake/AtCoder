N=int(input())
h=list(map(int,input().split()))

dp=[float('inf')]*N
dp[0]=0

for i in range(1,N):
    if 1<N:
        dp[i]=min(dp[i-2]+abs(h[i]-h[i-2]),dp[i-1]+abs(h[i]-h[i-1]))
    else:
        dp[i]=dp[i-1]+h[i]

print(dp[-1])