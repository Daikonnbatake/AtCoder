N,M,X=map(int,input().split())
ans=-1
C=[]; A=[]
flag=[[]]*(1<<N)

#bitマスク生成
for i in range(1<<N):
    d=[0]*N
    for j in range(N):
        if (i>>j)&1==1: d[j]=1
    flag[i]=d
#入力
for i in range(N):
    inp=list(map(int,input().split()))
    C.append(inp[0]); A.append(inp[1:])
#処理
for i in range(1<<N):
    f=flag[i]
    exp=[0]*M; yen=0
    for j in range(N):
        a=A[j]
        if f[j]==1:
            for k in range(M): exp[k]+=a[k]
            yen+=C[j]
    ok=True
    for j in range(M):
        if exp[j] < X: ok=False
    if ok: ans=min(ans,yen) if ans!=-1 else yen
print(ans)