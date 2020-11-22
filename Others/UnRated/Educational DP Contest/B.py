N,K=map(int,input().split())
h=list(map(int,input().split()))
 
inf = 1000000000
dp=[inf]*N
dp[0]=0
 
for i in range(1,N):
    m=inf
    for j in range(min(i,K)):
        a=abs(h[i]-h[i-j-1])+dp[i-j-1]
        if a<m:m=a
    dp[i]=m
print(dp[-1])