from decimal import Decimal as d
N=int(input())
ans=d(0)
for i in range(1,N):ans+=d(N)/d(N-i)
print(ans)