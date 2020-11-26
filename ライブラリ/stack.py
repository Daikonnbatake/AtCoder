from collections import deque
from itertools import islice

class Stack():
    def __init__(self):self.stack = deque()
    def __len__(self): return len(self.stack)
    def __str__(self): return str(self.stack)
    def __getitem__(self, item):
        left = item.start
        right = item.stop
        if left == None: left=0
        if right == None: right=len(self)
        if left<0:left+=len(self)
        if right<0:right+=len(self)
        return islice(self.stack, left, right)

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()