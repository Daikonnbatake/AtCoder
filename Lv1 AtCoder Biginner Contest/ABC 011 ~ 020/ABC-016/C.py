N,M=map(int,input().split())
ab=[list(map(int,input().split()))for i in range(M)]
g=[[0]*N for i in range(N)]

for a,b in ab:
    g[a-1][b-1]=1
    g[b-1][a-1]=1

# ユーザーを一人一人見る
for i in range(N):
    ff=[0]*N
    # ユーザーの友達を見る
    for j in range(N):
        if g[i][j]:
            #友達の友達を見る
            for k in range(N):
                if g[j][k] and g[i][k]!=1 and k!=i: ff[k] = 1
    print(sum(ff))