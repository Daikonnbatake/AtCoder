N=int(input())
ans=0
for i in range(1,int(N**0.5)+1):
    if int(str(i)*2)<=N:ans+=1
print(ans)