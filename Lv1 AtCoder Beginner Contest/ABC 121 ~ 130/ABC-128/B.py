N=int(input())
d=dict()
for i  in range(N):
    S,P=input().split()
    P=int(P)
    if S in d: d[S].append((P,i+1))
    else: d[S]=[(P,i+1)]

for i in [i[1] for i in sorted(d.items(), key=lambda x:x[0])]:
    i=sorted(i, key=lambda x: -x[0])
    for j in i:print(j[1])