def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)
N=int(input())
ans=0
for i in range(1,N+1): ans += i * rsum(N//i)
print(ans)