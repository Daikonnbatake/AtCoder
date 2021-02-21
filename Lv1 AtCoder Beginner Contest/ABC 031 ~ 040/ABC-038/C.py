def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)
N=int(input())
a=list(map(int,input().split()))

ans=0
l,r=0,0
a.append(0)

for i in range(N):
    if a[i-1] >= a[i]:
        ans+=rsum(r-l)
        l=r
    r+=1
print(ans+rsum(r-l))