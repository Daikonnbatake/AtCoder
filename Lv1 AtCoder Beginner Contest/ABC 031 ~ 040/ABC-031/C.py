def getT(t,l):
    m=50*-50
    N=len(l)
    for a in range(N):
        a=N-a-1
        if a==t:continue
        if a<t:
            s=sum(l[a+1:t+1:2])
            if m<=s:m,A,T=s,a,t+1
        else:
            s=sum(l[t+1:a+1:2])
            if m<=s:m,A,T=s,a+1,t
    if T<A:A,T=T,A
    return l[A:T]

N=int(input())
a=list(map(int,input().split()))
ans=50*-50

for i in range(N):
    ans=max(ans,sum(getT(i,a)[::2]))
print(ans)