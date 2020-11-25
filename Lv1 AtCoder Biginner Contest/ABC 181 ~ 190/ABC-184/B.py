N,X=map(int,input().split())
S=list(input())
p = X
for i in S:
    p=max(0,(p+(1 if i=='o' else -1)))

print(p)