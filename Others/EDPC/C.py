N=int(input())
l=[list(map(int,input().split()))for i in range(N)]
dp=[[0, 0, 0] for i in range(N)]

for i in range(1, N):
    a,b,c=dp[i-1]
    
    dp[i][0] = max(b+l[i-1][1], c+l[i-1][2])
    dp[i][1] = max(a+l[i-1][0], c+l[i-1][2])
    dp[i][2] = max(a+l[i-1][0], b+l[i-1][1])

dp[-1][0] += l[-1][0]
dp[-1][1] += l[-1][1]
dp[-1][2] += l[-1][2]

print(max(dp[-1]))