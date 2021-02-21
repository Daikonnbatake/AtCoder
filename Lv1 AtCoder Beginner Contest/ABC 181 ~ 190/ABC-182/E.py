H,W,N,M=map(int,input().split())
g=[[0]*W for i in range(H)]

# 1 は光源 2 はブロック

for i in range(N):
    a,b=map(int,input().split())
    g[a-1][b-1]=1
for i in range(M):
    a,b=map(int,input().split())
    g[a-1][b-1]=2



for i in g:print(i)