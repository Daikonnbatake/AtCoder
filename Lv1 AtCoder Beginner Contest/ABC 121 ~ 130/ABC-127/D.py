N,M=map(int,input().split())
A=sorted(list(map(int,input().split())))
ans=0
mask=[0]*N

query=dict()
for b,c in [map(int,input().split()) for i in range(M)]:
    if c in query: query[c]+=b
    else: query[c]=b

for c,b in sorted(query.items(), key=lambda x: -x[1]):
    mask[min(N-1,b-1)]=max(mask[min(N-1,b-1)], c)

for i in range(1,N):
    i=N-i-1
    mask[i]=max(mask[i+1],mask[i])

for i in range(N):ans+=max(A[i],mask[i])

print(ans)
print(A)
print(mask)