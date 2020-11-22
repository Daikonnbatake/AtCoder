from collections import deque
from itertools import islice

class Stack():
    def __init__(self): self.stack = deque()
    def __len__(self): return len(self.stack)
    def __str__(self): return str(self.stack)
    
    def __getitem__(self, l=0, r=-1):
        print(l,r)

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()

stack = Stack()
for i in range(10):
    stack.push(chr(97+i))

print(stack[-3:])
print(stack)