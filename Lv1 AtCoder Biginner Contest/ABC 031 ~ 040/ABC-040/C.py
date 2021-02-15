N=int(input())
a=list(map(int,input().split()))
a.append(a[0])

dp=[0]*N

for i in range(1,N):
    x = dp[i-1] + abs(a[i-1]-a[i])
    y = dp[i-2] + abs(a[i-2]-a[i])
    dp[i]=min(x,y)

print(dp[-1])