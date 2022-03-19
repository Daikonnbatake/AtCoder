N,K=map(int,input().split())
a=list(map(int,input().split()))
m=[k for j,k in sorted([(a[i],i) for i in range(N)],key=lambda x: x[0])]
base=K//N
plus=K%N
ans=[base]*N

for i in range(plus):ans[m[i]]+=1
for i in ans:print(i)