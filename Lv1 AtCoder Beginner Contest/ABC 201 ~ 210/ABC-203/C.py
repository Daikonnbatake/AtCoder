N,K=map(int,input().split())
AB=sorted([list(map(int,input().split())) for i in range(N)], key=lambda x: x[0])

f = dict()
p = dict()
q = set()

for a,b in AB:
    if a in f: f[a].append(b)
    else: f[a] = [b]

for i in range(N):
    if AB[i][0] in q:continue
    p[i] = AB[i][0]
    q.add(AB[i][0])

before = 0
for i in p.values():

    if K-(i-before)<0: break
    K+=sum(f[i])-(i-before)
    before = i

print(K+before)