N,X=map(int,input().split())
ans=1
a=0
for L in map(int,input().split()):
    a+=L
    if X<a:break
    ans+=1
print(ans)