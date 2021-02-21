import heapq
class Heap():
    def __init__(self,l):self.h=l;heapq.heapify(self.h)
    def push(self,x): heapq.heappush(self.h,x)
    def pop(self): return heapq.heappop(self.h)
    def get(self): return self.h

N,M=map(int,input().split())
A=Heap(list(map(lambda x:int(x)*-1,input().split())))

for i in range(M):A.push((A.pop()*-1)//2*-1)

print(sum(A.get())*-1)