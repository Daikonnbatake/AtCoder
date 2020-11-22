N=int(input())
a=list(map(int,input().split()))
h=[[]]*N
for i in range(N):h[i]=[a[i],i+1]
h.sort(key=lambda x: x[0])
for i in range(N):print(h[N-i-1][1])