from decimal import Decimal as d
A,B,C=map(int,input().split())
a,b,c=0,0,0
x = d(str(A+B+C))

a = (d(str(A))/x)*d(str(100-A))
b = (d(str(B))/x)*d(str(100-B))
c = (d(str(C))/x)*d(str(100-C))

print(a+b+c)