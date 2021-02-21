N,K=map(int,input().split())
A=list(map(int,input().split()))
f=[0]*N
l,r=[],[]
p=0
while f[p]<2:
    if f[p]:
        r.append(A[p])
        K+=1
    else:
        l.append(A[p])
        K-=1
    f[p]+=1
    p=A[p]-1
print(r[K%len(r)-1])