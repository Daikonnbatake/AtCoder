def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)

N,K=map(int,input().split())
mod=10**9+7
ans=0

for i in range(K,N+2):
    MIN=rsum(i-1)
    MAX=rsum(N)-rsum(N-i)
    ans = (ans + MAX-MIN+1)%mod

print(ans)