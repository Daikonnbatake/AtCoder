N,M=map(int,input().split())
A=sorted(list(map(int,input().split())))

if 0<M:
    l=[0]*(M+1)
    l[0]=A[0]-1
    if A[-1]!=N: l[-1]=N-A[-1]
    k=l[0] if 0<l[0] else 10**9
    ans=0

    for i in range(1,M):
        l[i]=A[i]-A[i-1]-1
        k=max(1,min(k,l[i]))
    
    k=k if l[-1]==0 else max(1,min(k,l[-1]))

    for i in range(M+1):
        if 0<l[i]:ans+=l[i]//k+1 if l[i]%k else l[i]//k

else:
    ans=1

print(ans)