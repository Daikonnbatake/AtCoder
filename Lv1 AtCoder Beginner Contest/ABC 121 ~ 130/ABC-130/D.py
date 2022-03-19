def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)

N,K=map(int,input().split())
a=list(map(int,input().split()))
ans=rsum(N)
r=0
m=0

for l in range(N):
    while r<N and m+a[r]<K:
        m+=a[r]
        r+=1
    m-=a[l]
    ans-=r-l

print(ans)