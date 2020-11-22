class Heap():
    def __init__(self):
        self.n = 0
        self.run = 0 # 配列をヒープに変換したときに正しくない要素を移動させた回数
        self.heap = [0]*self.n
    
    def push(self, x):
        self.heap.append(x)
        self.n += 1
        i = self.n - 1
        while i>0:
            p = (i-1)//2
            if self.heap[p] >= x:break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x

h = Heap()

for i in [1,2,3,4,7,8,9,10,14,16]:h.push(i)

print(h.heap)