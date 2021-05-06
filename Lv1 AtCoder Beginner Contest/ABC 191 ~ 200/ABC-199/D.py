from collections import deque
import math as m
class Queue():
    def __init__(self):self.queue = deque()
    def __len__(self): return len(self.queue)
    def enqueue(self, value):self.queue.append(value)
    def dequeue(self):return self.queue.popleft()

def permutation(n,r):
    a,b=0,0
    for i in range(n-r): a=(a*(i+1))
    for i in range(n): b=(b*(i+1))
    return b//a

def bfs(start,G):
    N=len(G)
    root=30
    if len(G)==0:return 3
    seen=[0]*N
    todo=Queue()
    todo.enqueue(start)
    score=0
    while 0<len(todo):
        now=todo.dequeue()
        c=0
        if seen[now]:continue
        root=min(root,now)
        seen[now]=1
        for i in G[now]:
            todo.enqueue(i)
            if seen[i]==0:c+=1
        if 2<c:score=-1
        if score!=-1:score+=3-c
    return (score,root)

N,M=map(int,input().split())
G=[[]for i in range(M)]
score=[0]*N
root=[0]*N
check=set()
ans=1
for i in range(M):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
if G==[[]for i in range(M)]:print(3**N);exit()

for i in range(N):score[i],root[i]=bfs(i,G)
for i in range(N):
    if root[i] in check:continue
    check.add(root[i])
    if score[i]:ans*=score[i]
print(ans if 0<ans else 0)