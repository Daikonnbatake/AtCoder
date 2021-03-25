import math as m
N=int(input())
C,S,F=[0]*(N-1),[0]*(N-1),[0]*(N-1)
for i in range(N-1):C[i],S[i],F[i]=map(int,input().split())

for i in range(N-1):
    time=0
    for j in range(i,N-1):
        time = max(m.ceil(time/F[j])*F[j],S[j]) +C[j]
    print(time)
print(0)