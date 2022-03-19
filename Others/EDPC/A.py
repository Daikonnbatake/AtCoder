N=int(input())
h=list(map(int,input().split()))

dp=[10000]*N
dp[0]=0

for i in range(1,N):
    if 1<i:
        dp[i] = min(dp[i-2] + abs(h[i-2]-h[i]), dp[i-1] + abs(h[i-1]-h[i]))
    else:
        dp[i] =dp[i-1] + abs(h[i-1]-h[i])
print(dp[-1])