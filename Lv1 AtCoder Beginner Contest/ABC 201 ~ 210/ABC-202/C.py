N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=0

#Aを辞書にする
d=dict()
for i in A:
    if i in d: d[i]+=1
    else: d[i]=1

for i in C:
    b=B[i-1]
    if b in d: ans+=d[b]

print(ans)