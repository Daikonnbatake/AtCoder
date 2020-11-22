N,M=map(int,input().split())
w=list(map(int,input().split()))
w.sort()
a=[[]for i in range(M)]
for i in range(M):a[i]=list(map(int,input().split()))
a.sort(key=lambda x: x[1])
print(a)