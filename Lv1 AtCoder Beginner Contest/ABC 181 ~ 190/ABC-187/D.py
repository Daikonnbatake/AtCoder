N=int(input())
L = [list(map(int,input().split()))for i in range(N)]
L.sort(key=lambda x: x[0]*2+x[1])

aoki = sum([a for a,b in L])
takahashi = 0
pos = N-1
ans = 0

while aoki >= takahashi:
    a,b = L[pos]
    aoki -= a
    takahashi += a+b
    pos -= 1
    ans+=1

print(ans)