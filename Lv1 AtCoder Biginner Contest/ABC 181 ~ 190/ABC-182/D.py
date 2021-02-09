N=int(input())
A=list(map(int,input().split()))

a,b = [0]*(N+1),[0]*(N+1)
ma = 0
ans = 0

for i in range(N):a[i+1] = a[i]+A[i]
for i in range(1,N):b[i+1] = b[i]+a[i]
for i in range(1,N+1):
    ma = max(ma,a[i])
    ans = max(ans,b[i]+ma)

print(ans)