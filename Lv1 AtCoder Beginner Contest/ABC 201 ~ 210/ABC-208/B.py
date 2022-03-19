P=int(input())
f=list(range(1,11))
for i in range(1,10):f[i]*=f[i-1]

ans=0
for i in range(10000):
    if P==0:break
    ans+=1
    for j in range(10):
        if P<f[j]:break
    P-=f[j-1]

print(ans)