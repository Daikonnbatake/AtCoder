from collections import deque
from itertools import islice
class Stack():
    def __init__(self,i):self.stack = deque(i)
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()
class Node():
    def __init__(self,to,cost):
        self.to=to
        self.cost=cost

N=int(input())
Graph=