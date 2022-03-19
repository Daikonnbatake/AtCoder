from collections import deque

class Stack():
    def __init__(self):self.stack = deque()
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()


N,M=map(int,input().split())
G=[[]*N for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
ans=0

def dfs(s):
    ret=0
    seen=[0]*N
    todo=Stack()
    todo.push(s)
    while 0<len(todo):
        now=todo.pop()
        if seen[now]:continue
        seen[now]=1
        ret+=1
        for i in G[now]: todo.push(i)

    return ret

for i in range(N):ans+=dfs(i)
print(ans)