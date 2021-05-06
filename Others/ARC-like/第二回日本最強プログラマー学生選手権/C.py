def p(n):
    if n == 1: return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i == 0: return False
    return True

A,B=map(int,input().split())
ans=0
a=[]
for i in range(1,int(100000**0.5)-1):
    for j in range(i+1,int(100000**0.5)):
        if A<=i*j and i*j<B:a.append()