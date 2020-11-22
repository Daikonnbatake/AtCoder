N = int(input())
g = [[-1]*N for i in range(N)]
ans=0
for i in range(N):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        g[i][x-1] = y
for i in range(1 << N):
    d=[0]*N
    for j in range(N):
        if (i >> j & 1) == 1:
            d[j] = 1
    ok = True
    for j in range(N):
        if d[j] == 1:
            for k in range(N):
                if g[j][k] == -1:
                    pass
                elif g[j][k] != d[k]:
                    ok = False
    if ok:
        ans = max(ans,d.count(1)) 
print(ans)