N=int(input())
ans=0
a,b=0,0
for i in range(N):
    x,y=map(int,input().split())
    if 0<i:ans+=abs(x-a)+abs(y-b)
    a,b=x,y
print(ans)