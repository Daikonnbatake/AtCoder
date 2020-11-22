import math
import decimal
N=int(input())
x=list(map(int,input().split()))
m=0
y=0
c=0
for i in x:
    m+=abs(i)
    y+=i*i
    c=max(c,abs(i))
print(m)
print(decimal.Decimal(y**0.5))
print(c)