from decimal import Decimal as d
X,Y,Z=map(d,input().split())
g=Y/X
ans=1
for i in range(10000):
    if g <= ans/Z:break
    ans+=1
print(ans-1)