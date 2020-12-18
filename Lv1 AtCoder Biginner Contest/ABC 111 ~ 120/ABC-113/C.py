from collections import deque  as d
def zero(n):return{1:'00000',2:'0000',3:'000',4:'00',5:'0',6:''}[len(str(n))]+str(n)

N,M=map(int,input().split())
index=[[0,0]for i in range(M)]
C=[d([])for i in range(N)]

for i in range(M):
    P,Y=map(int,input().split())
    C[P-1].append([Y,i])

for i in range(N):
    C[i]=sorted(C[i],key=lambda x: x[0])
    for j in range(len(C[i])):index[C[i][j][1]]=[i,j]

for i in index:
    print(zero(i[0]+1)+zero(i[1]+1))