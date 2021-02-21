N=int(input())
A=list(map(int,input().split()))
ok=True
ans=0
while ok==True:
    for i in range(N):
        if A[i]%2:ok=False
        A[i]=A[i]//2
    if ok:ans+=1
print(ans)