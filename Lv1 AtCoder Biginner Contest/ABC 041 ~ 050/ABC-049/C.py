from collections import deque
class Stack():
    def __init__(self,l):self.stack = deque(l)
    def __len__(self): return len(self.stack)
    def push(self, value):self.stack.append(value)
    def pop(self):return self.stack.pop()
S=Stack(list(input()))
m=''
c=set(['dream','dreamer','erase','eraser'])
for i in range(len(S)):
    m=S.pop()+m
    if m in c:m=''
print('YNEOS'[m!=''::2])