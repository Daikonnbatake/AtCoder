N=list(map(int,list(input())))
l=len(N)
if 1<l:
    ans=20
    for i in range(1<<l):
        m=0
        c=0
        for j in range(l):
            if i&1<<j:
                m+=N[j]
            else:c+=1
        if not m%3:
            ans=min(ans,c)
    print(ans if l!=ans else -1)
else:
    print(-1 if N[0]%3 else 0)