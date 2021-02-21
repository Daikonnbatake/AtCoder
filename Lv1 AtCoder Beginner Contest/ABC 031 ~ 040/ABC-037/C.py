N,K=map(int,input().split())
a=list(map(int,input().split()))
n=sum(a[0:K])
b=[0]*(N-K+1);b[0]=n
for i in range(K,N):
    n+=a[i]-a[i-K]
    b[i-K+1]=n
print(sum(b))