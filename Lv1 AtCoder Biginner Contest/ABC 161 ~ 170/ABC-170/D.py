N=int(input())
A=list(map(int,input().split()))
MAX=max(A)
l=[0]*(10**6)
ans=0

for i in A:
    j=1
    while j*i<=MAX:
        if j==1: l[j*i-1]+=1
        else: l[j*i-1]=2
        j+=1
for i in A:
    if l[i-1]<2:ans+=1

print(ans)