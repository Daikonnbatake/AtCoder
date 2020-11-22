import itertools as itr
N,K=map(int,input().split())
T=[list(map(int,input().split()))for i in range(N)]

a = list(itr.permutations([i+1 for i in range(1,N)]))
ans=0

for i in range(len(a)):
    l=[1]
    l.extend(a[i])
    l.append(1)
    m=0
    for j in range(N+1):
        m+=T[l[j-1]-1][l[j]-1]
    if m==K:ans+=1

print(ans)