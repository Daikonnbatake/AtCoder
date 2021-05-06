from collections import deque
class Stack():
    def __init__(self):self.stack = deque()
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()
S=list(input())
N=len(S)
s=Stack()
R=0
T=['']*(10**6+10)
l,r=(10**6+10)//2,(10**6+10)//2+1
for i in S:
    if i=='R':R= (0 if R else 1)
    else:
        if R:T[l]=i;l-=1
        else:T[r]=i;r+=1
T=''.join(T)
stack=Stack()
for i in range(len(T)):
    end=(stack.pop() if 0<len(stack)else'')
    if end!=T[i]:
        stack.push(end)
        stack.push(T[i])

if not r:print(''.join(stack.stack))
else:print(''.join([stack.pop for i in range(len(stack))]))