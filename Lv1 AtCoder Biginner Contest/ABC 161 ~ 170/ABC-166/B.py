N,K=map(int,input().split())
snuke=[0]*N
for i in range(K):
    d=int(input())
    A=list(map(int,input().split()))
    for j in range(d):
        snuke[A[j]-1] += 1
ans=0
for i in snuke:
    if i==0:
        ans+=1
print(ans)