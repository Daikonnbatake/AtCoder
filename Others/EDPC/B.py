N,K=map(int,input().split())
h=list(map(int,input().split()))

inf=10**9
dp=[inf]*N
dp[0]=0

for i in range(1, N):
    m=inf
    for j in range(min(K,i)):
        a=abs(h[i]-h[i-j-1])+dp[i-j-1]
        m=min(m,a)
    dp[i]=m

print(dp[-1])