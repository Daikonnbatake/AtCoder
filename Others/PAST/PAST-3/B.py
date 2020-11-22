N,M,Q=map(int,input().split())
s=[[0]*M for i in range(N)]
q=[0]*M
p=[0]*M
for i in range(Q):
    inp=list(map(int,input().split()))
    D=inp[0]
    if D==1: n=inp[1]-1
    else: n=inp[1]-1; m=inp[2]-1

    #クエリ1
    if D==1:
        ans=0
        for j in range(M):
            if s[n][j]==1: ans+=p[j]
        print(ans)
    #クエリ2
    if D==2:
        q[m]+=1
        s[n][m]=1
        p[m]=N-q[m]