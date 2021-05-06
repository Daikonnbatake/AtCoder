from collections import deque
class Queue():
    def __init__(self):self.queue = deque()
    def __len__(self): return len(self.queue)
    def enqueue(self, value):self.queue.append(value)
    def dequeue(self):return self.queue.popleft()

H,W=map(int,input().split())
S=[tuple(input())for i in range(H)]
inf=float('inf')
seen=[[inf]*W for i in range(H)]
todo=Queue()
todo.enqueue((0,0))
ans=H*W

for i in S:
    for j in i:
        if j=='#':ans-=1

while 0<len(todo):
    y,x=todo.dequeue()
    if seen[y][x]!=inf:continue
    if 0<=y-1:
        if seen[y-1][x]==inf and S[y-1][x]=='.':todo.enqueue((y-1,x))
        seen[y][x]=min(seen[y][x],seen[y-1][x]+1)
    if y+1<H:
        if seen[y+1][x]==inf and S[y+1][x]=='.':todo.enqueue((y+1,x))
        seen[y][x]=min(seen[y][x],seen[y+1][x]+1)
    if 0<=x-1:
        if seen[y][x-1]==inf and S[y][x-1]=='.':todo.enqueue((y,x-1))
        seen[y][x]=min(seen[y][x],seen[y][x-1]+1)
    if x+1<W:
        if seen[y][x+1]==inf and S[y][x+1]=='.':todo.enqueue((y,x+1))
        seen[y][x]=min(seen[y][x],seen[y][x+1]+1)
    if x==0 and y==0:seen[y][x]=0

if seen[-1][-1]==inf:print(-1)
else:print(ans-seen[-1][-1]-1)