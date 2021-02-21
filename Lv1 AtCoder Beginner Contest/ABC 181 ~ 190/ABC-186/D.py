N=int(input())
A=list(map(int,input().split()))

A.sort()
a=[0]*(N+1)

ans=0

for i in range(1,N+1): a[N-i]+=a[N-i+1]+A[N-i]
for i in range(N):ans+=abs((N-i-1)*A[i]-a[i+1])

print(ans)