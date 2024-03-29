N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(N):
    ai, bi = AB[i]
    for j in range(N):
        aj, bj = AB[j]
        time = ai + bj if i == j else max(ai, bj)
        ans = min(ans, time)
print(ans)