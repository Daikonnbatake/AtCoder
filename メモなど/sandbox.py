from collections import deque 
H,W=map(int,input().split())
c=[[]for i in range(H)]
V=[[]for i in range(H*W)]
c.insert(0,['#']*(W+2))
c.append(['#']*(W+2))
f=set(['s','g','.'])
for i in range(1,H+1):
    c[i]=list(input())
    c[i].insert(0,'#');c[i].append('#')
    if 's'in c[i]:sx,sy=c[i].index('s'),i
    if 'g'in c[i]:gx,gy=c[i].index('g'),i
for i in range(1,H+1):
    for j in range(1,W+1):
        C=i*W+j-W-1
        if c[i][j]in f:
            if c[i-1][j]in f:V[C].append(C-W);V[C-W].append(C)
            if c[i+1][j]in f:V[C].append(C+W);V[C+W].append(C)
            if c[i][j-1]in f:V[C].append(C-1);V[C-1].append(C)
            if c[i][j+1]in f:V[C].append(C+1);V[C+1].append(C)
stack=deque([sx*W+xy])
seen=[0]*(H*W)
while 0<len(stack):
    for i in V[stack.pop()]:
        if seen[i]==0:
            seen[i]=1

for i in V:print(i)