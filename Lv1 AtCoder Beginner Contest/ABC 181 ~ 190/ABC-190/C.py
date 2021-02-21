N,M=map(int,input().split())
ab=[list(map(int,input().split()))for i in range(M)]
K=int(input())
cd=[list(map(int,input().split()))for i in range(K)]
ans=0

for i in range(1<<K):
    D=[0]*N
    m=0
    for j in range(K):
        if i>>j&1: D[cd[j][1]-1]=1
        else: D[cd[j][0]-1]=1
    for a,b in ab:
        if D[a-1]==1 and D[b-1]==1: m+=1
    ans=max(ans,m)

print(ans)