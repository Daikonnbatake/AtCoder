N, M=map(int, input().split())

ans = 0
v = [set([i])for i in range(N)]

for i in range(M):
    x, y=map(int, input().split())
    x-=1; y-=1
    v[x].add(y)
    v[y].add(x)

for i in range(1,1<<N):
    s = set()
    m = 0
    for j in range(N):
        if i & 1<<j:
            s.add(j)
    for j in s:
        if s & v[j] == s:
            m += 1
    ans = max(ans, m)
print(ans)