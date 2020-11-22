from collections import deque
from itertools import islice

class Queue():
    def __init__(self):self.queue = deque()
    def __len__(self): return len(self.queue)
    def __str__(self): return str(self.queue)
    def __getitem__(self, item):
        left = item.start
        right = item.stop
        if left == None: left=0
        if right == None: right=len(self)
        if left<0:left+=len(self)
        if right<0:right+=len(self)
        return islice(self.queue, left, right)

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.popleft()