N=int(input())
A=list(map(int,input().split()))
w,h=[0]*N+1,[0]*N
w[0]=A[0]
ans=0
a,b=A[0],0
for i in range(1,N+1):
    w[i]=w[i-1]+A[i]
    h[i]=w[i-1]+h[i-1]
    a,b=max(a,w[i]),max(b,h[i])
    ans=max(ans,a+b)
print(ans)