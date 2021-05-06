import sys
sys.setrecursionlimit(1000000)

N=int(input())
G=[[]for i in range(N)]
color=[0]*N
seen=[0]*N

for i in range(N-1):
    u,v,w=map(int,input().split())
    G[u-1].append([v-1,w%2])
    G[v-1].append([u-1,w%2])

def dfs(now,pc):
    if seen[now]:return
    seen[now]=1
    color[now]=pc
    for i,c in G[now]:
        dfs(i,(pc+c)%2)
dfs(0,0)
for i in color:print(i)