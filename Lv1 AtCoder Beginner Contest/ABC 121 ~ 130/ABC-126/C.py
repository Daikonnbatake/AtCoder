from decimal import Decimal as d
import decimal

def f(n, k):
    ret=0
    while n<k:
        ret+=1
        n*=2
    return ret

N,K=map(int,input().split())
ans=d('0')

base=d('1')/d(str(N))
for i in range(1,N+1):ans+=base * pow(d('0.5'), f(i, K))

print(ans)