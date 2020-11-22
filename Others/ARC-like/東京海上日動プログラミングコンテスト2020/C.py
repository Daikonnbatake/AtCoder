N,K=map(int,input().split())
A=list(map(int,input().split()))
ruiseki=[0]*N
ans=[0]*N
a=0
for i in range(N):
    a=A[i]*K
    ruiseki[max(0,i-a-1)]+=a
    if i+a+1 < N-1:
        ruiseki[i+a+1]-=a
    print(ruiseki)
ans[0]=ruiseki[0]
for i in range(1,N): ans[i]=ans[i-1]+ruiseki[i]
print(''.join(map(str,ans)))