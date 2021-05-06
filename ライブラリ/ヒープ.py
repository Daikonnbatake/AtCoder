import heapq

class Heap():
    def __init__(self,l=[]):
        if len(l):self.heap=heapq.heapify(l)
        else:self.heap=l
    def push(self,n):heappush(self.heap,n)
    def pop(self):heappop(self.heap)