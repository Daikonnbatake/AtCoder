N,M=map(int,input().split())
ab=[list(map(int,input().split()))for i in range(M)]
K=int(input())
C=list(map(int,input().split()))

o=[set()for i in range(N)]
s=[0]*N

for a,b in ab:
    o[a-1].add(b-1)
    o[b-1].add(a-1)

print(o)