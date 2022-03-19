N=int(input())
T=sorted(list(map(int,input().split())))
A,B=0,0

for i in range(N):
    if A<B:A+=T[i]
    else:B+=T[i]

print(max(A,B))