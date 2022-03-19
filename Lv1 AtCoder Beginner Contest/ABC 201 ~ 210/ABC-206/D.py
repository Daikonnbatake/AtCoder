from collections import deque

N=int(input())
A=deque(list(map(int,input().split())))
D=dict()
ans=0

for i in range(N//2):
    l,r=str(A.popleft()),str(A.pop())

    if l==r: continue
    if l in D:D[l].add(r)
    else:D[l]=set([r])

    if r in D:D[r].add(l)
    else:D[r]=set([l])
    ans+=1

key=''
m=0
for k,v in D.items():
    if m<len(v):key=k

print(len(D[key]))