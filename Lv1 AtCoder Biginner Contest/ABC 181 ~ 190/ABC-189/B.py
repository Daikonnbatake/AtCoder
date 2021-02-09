N,X=map(int,input().split())

ans=0
al=0

for i in range(N):
    V,P=map(int,input().split())
    ans += 1
    al += V*P
    if X*100<al:
        print(ans)
        exit()
print(-1)