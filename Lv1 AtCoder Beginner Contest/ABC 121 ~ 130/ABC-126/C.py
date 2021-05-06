from decimal import Decimal as d
from decimal import getcontext as g

N,K=map(int,input().split())
ans=d('0')
for i in range(1,N+1):
    m=i
    c=0
    while m<K:
        c+=1
        m*=2
    ans+=d('1')/d(str(pow(2,c)*N))
print(ans)