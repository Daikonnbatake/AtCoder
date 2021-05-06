from collections import deque
class Stack():
    def __init__(self):self.stack = deque()
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()

N,Q=map(int,input().split())
G=[[]for i in range(N)]
todo=Stack()
todo.push(0)
seen,cost=[0]*N,[0]*N

for i in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for i in range(Q):
    p,x=map(int,input().split())
    p-=1
    cost[p]+=x

while 0!=len(todo):
    now=todo.pop()
    if seen[now]==2:continue
    for i in G[now]:
        todo.push(i)
        if 0<seen[i]:continue
        seen[i]=1
        cost[i]+=cost[now]
    seen[now]=2

print(' '.join(map(str,cost)))