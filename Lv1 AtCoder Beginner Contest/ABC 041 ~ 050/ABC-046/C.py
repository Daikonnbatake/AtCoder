N=int(input())
t,a=1,1
for i in range(N):
    T,A=map(int,input().split())
    n=max(-(-t//T),-(-a//A))
    t,a=n*T,n*A
print(a+t)