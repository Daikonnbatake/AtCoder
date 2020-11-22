import itertools
import math
N=int(input())
l=[]
mem=[]
P=list(itertools.permutations(range(1,N+1)))
for i in range(N):
    l.append(list(map(int,input().split())))
for i in range(len(P)):
    mem.append(0)
    for j in range(len(P[i])-1):
        pos1 = P[i][j]-1
        pos2 = P[i][j+1]-1
        mem[i] += math.sqrt(((l[pos1][0]-l[pos2][0])**2) + ((l[pos1][1]-l[pos2][1])**2))
print(sum(mem)/len(mem))
print(mem)