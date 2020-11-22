N,W=map(int,input().split())

t=[0]*200002
for i in range(N):
    S,T,P=map(int,input().split())
    t[S]+=P
    t[T]-=P

for i in range(1,200001):
    t[i]=t[i-1]+t[i]

print('No'if max(t)>W else'Yes')