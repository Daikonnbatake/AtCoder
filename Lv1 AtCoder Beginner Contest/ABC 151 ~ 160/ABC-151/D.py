from collections import deque
class Queue():
    def __init__(self,l):self.queue = deque(l)
    def __len__(self): return len(self.queue)
    def enqueue(self,value):self.queue.append(value)
    def dequeue(self):return self.queue.popleft()

H,W=map(int,input().split())
S=['#'+input()+'#' for i in range(H)]
S.insert(0,'#'*(W+2))
S.append('#'*(W+2))
inf=1000
a,b,c,d=[inf,inf],[inf,0],[0,inf],[0,0]
ans=0

def bfs(sx,sy):
    seen=[[inf]*(W+2) for i in range(H+2)]
    todo=Queue([[sx,sy]])
    mc=0
    while 0<len(todo):
        pos=todo.dequeue()
        x,y=pos
        if seen[y][x]<inf or S[y][x]=='#':continue
        if S[y][x-1]=='.':todo.enqueue([x-1,y])
        if S[y][x+1]=='.':todo.enqueue([x+1,y])
        if S[y-1][x]=='.':todo.enqueue([x,y-1])
        if S[y+1][x]=='.':todo.enqueue([x,y+1])
        if x==sx and y==sy:seen[y][x]=0
        else:seen[y][x]=min(seen[y][x-1],seen[y][x+1],seen[y-1][x],seen[y+1][x])+1
        mc=max(mc,seen[y][x])
    return mc

for i in range(1,H+1):
    for j in range(1,W+1):
        ans=max(ans,bfs(j,i))

print(ans)