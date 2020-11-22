import decimal
a,b,c,d=map(int,input().split())
print(decimal.Decimal(((a*d)+(c*b))/(b+d)))