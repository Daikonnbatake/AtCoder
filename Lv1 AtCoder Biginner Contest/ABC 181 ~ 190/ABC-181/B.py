def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)
N=int(input())
ans=0
for i in range(N):
    A,B=map(int,input().split())
    ans+=rsum(B)-rsum(A-1)
print(ans)