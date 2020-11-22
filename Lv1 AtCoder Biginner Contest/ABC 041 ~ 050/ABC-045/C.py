S=list(input())
n=len(S)
ans=0
for i in range(2**(n-1)):
    stack=""
    l=[]
    for j in range(n):
        stack=stack+S[j]
        if ((i >> j) & 1)or j==n-1:
            l.append(int(stack))
            stack=""
    ans+=sum(l)
print(ans)