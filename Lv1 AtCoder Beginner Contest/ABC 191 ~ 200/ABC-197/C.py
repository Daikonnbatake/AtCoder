N=int(input())
A=list(map(int,input().split()))
ans=10**10

for i in range(1<<N):
    m=0
    a=[]
    for j in range(N):
        m|=A[j]
        if i>>j&1:
            a.append(m)
            m=0
    a.append(m)
    t=a[0]
    for j in range(1,len(a)):t^=a[j]
    ans=min(ans,t)
print(ans)