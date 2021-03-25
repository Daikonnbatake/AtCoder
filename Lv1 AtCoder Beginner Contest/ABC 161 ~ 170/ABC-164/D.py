S=input()
N=len(S)
l,r=0,0

c=list(map(int,list(S)))
a=[0]*(N+1)
for i in range(1,N+1):a[i]=c[i-1]+a[i-1]

print(a)