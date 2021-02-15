K=int(input())
ans=-1
m=7

def f(x):return (x*10+7)%K

for i in range(1,K+1):
    if m % K==0:
        ans=i
        break
    m=f(m)

print(ans)