from collections import deque
class Stack():
    def __init__(self,l):self.stack = deque(l)
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()
 
N=int(input())
C=list(map(int,input().split()))
G=[[]for i in range(N)]
 
for i in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
 
todo=Stack([0])
seen=[0]*N
colors=[set()for i in range(N)]
colors[0].add(C[0])
check=[0]*N
 
while 0<len(todo):
    now=todo.pop()
    if seen[now]:continue
    seen[now]=1
    c=colors[now].copy()
    for i in G[now]:
        todo.push(i)
        if not C[i] in colors[now]:check[i]=1
        colors[i]=c
        colors[i].add(C[i])

print(1)
for i in range(N):
    if check[i]:print(i+1)