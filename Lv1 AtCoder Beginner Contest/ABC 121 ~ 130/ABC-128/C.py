N,M=map(int,input().split())
k,s=[0]*M,[[]for i in range(M)]
for i in range(M):
    tmp=list(map(int,input().split()))
    k[i]=tmp[0]
    s[i]=tmp[1:]
p=list(map(int,input().split()))

ans=0
for i in range(1<<N):
    S=[0]*N
    f=False
    for j in range(N):S[j]=i>>j&1
    for j in range(M):
        m=0
        for l in range(k[j]):m=(m+S[s[j][l]-1])%2
        if p[j]!=m:
            f=True
            break
    if f:continue
    ans+=1
print(ans)