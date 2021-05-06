N,M=map(int,input().split())
l=[list(map(int,input().split()))for i in range(M)]
p=list(map(int,input().split()))
ans=0
for i in range(1<<N):
    s=[0]*N
    ok=True
    for j in range(N):
        if i>>j&1:s[j]=1
    for j in range(M):
        m=0
        for k in range(1,l[j][0]+1):
            if s[l[j][k]-1]:m+=1
        if m%2!=p[j]:ok=False
    if ok:ans+=1
print(ans)