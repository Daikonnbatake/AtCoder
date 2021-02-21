N,M=map(int,input().split())
L=[[]for i in range(M)]
for i in range(M):L[i]=list(map(int,input().split()))[1:]
p=list(map(int,input().split()))
ans=0

for i in range(1<<N):
    l=[0]*N
    q=[0]*M
    for j in range(N):l[j]=i>>j&1
    for j in range(M):
        for k in L[j]:
            q[j]+=1 if l[k-1]else 0
    for j in range(M):q[j]%=2
    if p==q:ans+=1
print(ans)