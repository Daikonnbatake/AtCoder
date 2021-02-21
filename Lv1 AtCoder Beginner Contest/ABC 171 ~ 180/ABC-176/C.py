N=int(input())
A=list(map(int,input().split()))
m=A[0]
ans=0
for i in A:
    ans+=abs(m-i)if i<=m else 0
    m=max(m,i)
print(ans)