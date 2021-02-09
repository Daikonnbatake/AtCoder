from collections import deque

class Stack():
    def __init__(self,l):self.stack = deque(l)
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()

X,Y=map(int,input().split())

max_x = 0
max_y = 0

if Y <= X*2 and X <= Y*2:
    pass
else:
    print(0)