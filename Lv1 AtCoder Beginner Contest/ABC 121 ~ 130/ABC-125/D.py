N=int(input())
A=tuple(map(int,input().split()))
p,m=0,0

for i in A:
    if i<0: m+=1
    else: p+=1

a=sum([abs(i) for i in A])

if m%2==0: print(a)
else:print(a-(min([abs(i) for i in A])*2))