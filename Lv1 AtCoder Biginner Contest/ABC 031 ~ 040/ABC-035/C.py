N,Q=map(int,input().split())
a=[0]*(N+1)
ans=[0]*N
for i in range(Q):
    l,r=map(int,input().split())
    a[l-1]+=1;a[r]-=1
m=a[0]
for i in range(1,N+1):
    ans[i-1]=m
    m+=a[i]
print(''.join(map(str,[i%2 for i in ans])))