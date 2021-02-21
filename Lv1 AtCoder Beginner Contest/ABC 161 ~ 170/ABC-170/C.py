X,N=map(int,input().split())
if N==0: print(X)
else:
    p=list(map(int,input().split()))
    m=10000
    ans=N
    for i in range(-101,101):
        if m>abs((i+1)-X) and not i+1 in p:
            m=abs((i+1)-X)
            ans=i+1
    print(ans)