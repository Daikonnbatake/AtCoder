N=int(input())
ans=0
a=0
for i in range(N):
    a+=i+1
    ans+=1
    if N<=a:
        print(ans)
        exit()