n=int(input())
L=[0]*((10**6)+2)
for i in range(n):
    a,b=map(int,input().split())
    L[a]+=1; L[b+1]-=1
m=0; ans=0
for i in range(len(L)):
    m+=L[i]; ans=max(ans,m)
print(ans)