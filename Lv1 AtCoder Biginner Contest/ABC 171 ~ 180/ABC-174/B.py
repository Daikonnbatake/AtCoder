import math
N,D=map(int,input().split())
ans=0
for i in range(N):
    X,Y=map(int,input().split())
    if math.sqrt(X**2 + Y**2)<=D:
        ans+=1
print(ans)