N,L=map(int,input().split())
mem=sum(range(L,L+N))
m=mem
ans=0
for i in range(N):
    tmp=(sum(range(L,L+N))-(L+i))
    if abs(mem-tmp) < abs(m):
        m=mem-tmp
        ans=tmp
print(ans)