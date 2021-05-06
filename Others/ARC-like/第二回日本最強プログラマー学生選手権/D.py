N,P=map(int,input().split())
mod=10**9+7
a=pow(P-1,N,mod)
b=a//P

print(P*(N-1)//N,a)