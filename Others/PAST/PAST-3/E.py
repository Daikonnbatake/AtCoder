N,M,Q=map(int,input().split())
S=[[0]*N for i in range(N)] #接続している頂点の情報
for i in range(M):
    u,v=map(int,input().split())
    S[u-1][v-1]=1; S[v-1][u-1]=1

c=list(map(int,input().split())) # 頂点の色情報

for i in range(Q):
    inp=list(map(int,input().split()))
    if inp[0]==1: x,D=inp[1]-1,1
    else: x,y,D=inp[1]-1,inp[2],2

    #クエリ1
    if D==1:
        print(c[x])
        for j in range(N):
            if S[x][j]==1: c[j]=c[x]
    
    #クエリ2
    if D==2:
        print(c[x])
        c[x]=y