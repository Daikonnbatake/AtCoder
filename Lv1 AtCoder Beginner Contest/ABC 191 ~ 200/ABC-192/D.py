def f(n,x,m):
    ret=0
    N=len(n)
    for i in range(N):
        ret += pow(x,N-i-1) * n[i]
        if m<ret:break
    return ret

X,M=list(map(int,list(input()))),int(input())
d=max(X)+1
l,r=d,M
ans=0

while l+1<r:
    m=(l+r)//2
    if f(X,m,M)<=M:l=m
    else:r=m

if len(X)<2: print(0 if M<d else 1)
else:print(max(0,m-d))