from collections import deque
class Queue():
    def __init__(self,l):self.queue = deque(l)
    def __len__(self): return len(self.queue)
    def enqueue(self, value):self.queue.append(value)
    def dequeue(self):return self.queue.popleft()

#入力
N,M=map(int,input().split())
Graph=[[]for i in range(N)]
cost=[[0]*N for i in range(N)]
# A→B のコストは cost[A-1][B-1] に格納される
for i in range(M):
    A,B,C=map(int,input().split())
    Graph[A-1].append(B-1)
    cost[A-1][B-1]=C

def bfs(start, constraint):
    todo=Queue([start])
    ret=[float('inf')]*N
    ret[start]=0
    seen=[0]*N
    while 0<len(todo):
        now=todo.dequeue()
        if seen[now]:continue
        if now!=start and constraint<now:continue
        seen[now]=1

        for i in Graph[now]:
            ret[i]=min(ret[i], ret[now]+cost[now][i])
            todo.enqueue(i)
    return ret

def S(l):
    ret=0
    for i in l:
        if i==float('inf'):continue
        ret+=i
    return ret

ans=0

for s in range(N):
    for k in range(N):
        ans+=S(bfs(s,k))

print(ans)