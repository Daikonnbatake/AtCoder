N=int(input())
a=list(map(int,input().split()))
ans=0
if sum(a)%N:print(-1)
else:
    for i in range(N-1):
        if sum(a[:i+1])//(i+1)!=sum(a)//N or sum(a[i+1:])//(N-i-1)!=sum(a)//N:ans+=1
    print(ans)