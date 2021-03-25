N,K=map(int,input().split())
a=list(map(int,input().split()))
ans=(N+1)*N//2
l,r=0,0
m=0
for i in range(N):
    while r<N and m+a[r]<K:m+=a[r];r+=1
    ans-=r-l
    m-=a[l]
    l+=1
            
print(ans)