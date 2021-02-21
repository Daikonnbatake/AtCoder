N,M=map(int,input().split())
X,Y=map(int,input().split())
a,b=[list(map(int,input().split()))for i in range(2)]
p,q,time,ans=0,0,0,0
while True:
    while a[p]<time and p<N-1: p+=1
    if a[p]<time:break
    time = a[p] + X
    while b[q]<time and q<M-1: q+=1
    time = b[q] + Y
    if a[p]+X <= b[q]: ans += 1
    if N-1==p or M-1==q:break
print(ans)