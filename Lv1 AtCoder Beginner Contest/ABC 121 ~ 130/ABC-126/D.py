import sys
sys.setrecursionlimit(10**9)

N=int(input())
G=[[]for i in range(N)]
seen=[0]*N

# G[i][0] = 接続先頂点, G[i][1] = 辺のコスト
for u,v,w in [map(int,input().split()) for i in range(N-1)]:
    G[u-1].append([v-1,w])
    G[v-1].append([u-1,w])

def dfs(now, cost):
    if seen[now]: return
    seen[now]=cost
    if now==0:seen[now]=1
    for v,w in G[now]:dfs(v, w+cost)
    return

dfs(0,0)
seen[0]=0

for i in seen: print(i%2)