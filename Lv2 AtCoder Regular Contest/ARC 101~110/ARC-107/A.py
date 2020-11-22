A,B,C=map(int,input().split())
mod = 998244353
ans=0

def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)

ans=rsum(C)%mod
ans=(ans*rsum(B))%mod
print(ans*rsum(A)%mod)