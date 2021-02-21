n,a,b=map(int,input().split())
mod=10**9+7
N,A,na,B,nb=1,1,1,1,1
for i in range(1,n+1):N=N*i%mod
for i in range(1,a+1):A=A*i%mod
for i in range(1,n-a+1):na=na*i%mod
for i in range(1,b+1):B=B*i%mod
for i in range(1,n-b+1):nb=nb*i%mod
print((pow(2,n,mod)-(N//(na*A))-(N//(na*B)))%mod)