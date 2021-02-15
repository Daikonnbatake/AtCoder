def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)

N=int(input())+1
l,r,m=1,N-1,0
if N==2:print(1)
else:
    while l+1!=r:
        m=(l+r)//2
        if rsum(m)<N: l=m
        else: r=m

    print(N-l if N<rsum(r) else N-r)