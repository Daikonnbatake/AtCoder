N=int(input())
W=list(map(int,input().split()))
ans=100
for i in range(N):
    a=W[:i]; b=W[i:]
    ans=min(ans,abs(sum(a)-sum(b)))
print(ans)