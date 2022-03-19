N,M=map(int,input().split())
s=[0]*(N+1)

for i in range(M):
    L,R=map(int,input().split())
    s[L-1]+=1
    s[R]-=1
for i in range(1,N+1):s[i]+=s[i-1]

print(s.count(M))