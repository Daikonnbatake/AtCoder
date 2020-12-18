def nn(n,x,k=-1):
    m=n;r=[]
    while 0<m:r.insert(0,m%x);m=m//x
    while len(r)<k:r.insert(0,0)
    return r

N,A,B,C=map(int,input().split())
l=sorted([int(input())for i in range(N)])

ans=10**10

for i in range(4**N):
    mask=nn(i,4,N)
    a,b,c=0,0,0
    mp=0
    for j in range(N):
        if mask[j]==1:
            if 0<a:mp+=10
            a+=l[j]
        if mask[j]==2:
            if 0<b:mp+=10
            b+=l[j]
        if mask[j]==3:
            if 0<c:mp+=10
            c+=l[j]
    if 0<min(a,b,c):ans=min(ans,abs(A-a)+abs(B-b)+abs(C-c)+mp)

print(ans)