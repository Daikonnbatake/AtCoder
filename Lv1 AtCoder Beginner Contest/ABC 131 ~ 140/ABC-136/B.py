N=int(input())
ans=0
for i in range(1,(10**5)+1):
    if len(str(i))%2==1: ans+=1
    if i==N: break
print(ans)