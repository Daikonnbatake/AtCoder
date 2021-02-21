import math
def combination(n,r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N=int(input())
mem={}
for i in range(N):
    s=list(input())
    s.sort()
    s=''.join(s)
    if s in mem: mem[s]+=1
    else: mem[s]=0
    count=0
for i in mem.values():
    if i!=0: count += combination(i+1,2)
print(count)