N=int(input())
m=10**10

for i in range(N):
    A,P,X=map(int,input().split())
    if A<X: m=min(m,P)

print(-1 if 10**9<m else m)