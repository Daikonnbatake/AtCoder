N,K=map(int,input().split())
t=[0]*N
for i in range(N): t[i]=int(input())
t.sort(key=int)
ans=10**10
for i in range(N-K+1): ans=min(ans,t[i+K-1]-t[i])
print(ans)