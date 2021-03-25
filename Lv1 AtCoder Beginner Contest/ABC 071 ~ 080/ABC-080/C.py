N=int(input())
F=[list(map(int,input().split()))for i in range(N)]
P=[list(map(int,input().split()))for i in range(N)]
ans=10**15*-1
for i in range(1,1<<10):
    p=[0]*N
    for j in range(10):
        if i>>j&1:
            for k in range(N):
                if F[k][j]:p[k]+=1
    ans=max(ans,sum([P[i][p[i]] for i in range(N)]))
print(ans)