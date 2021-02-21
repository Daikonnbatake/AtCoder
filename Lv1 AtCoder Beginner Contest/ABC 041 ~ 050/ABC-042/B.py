N,L=map(int,input().split())
S=[input() for i in range(N)]
S.sort()
s=""
for i in S:
    s=s+i
print(s)