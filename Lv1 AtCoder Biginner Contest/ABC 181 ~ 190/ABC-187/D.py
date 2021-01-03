N=int(input())
p=[list(map(int,input().split()))for i in range(N)]
p.sort(key=lambda x: x[0])

aoki=0
takahashi=0

ans=0

for a,t in p:takahashi+=a+t

for a,t in p:
    aoki += a
    takahashi -= a+t
    if aoki >= takahashi: break
    ans+=1

print(N-ans)