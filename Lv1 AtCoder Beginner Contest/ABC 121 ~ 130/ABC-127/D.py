import bisect
class BinSearch():
    def __init__(self,l):self.l = l
    def under_n(self,n):return bisect.bisect_right(self.l,n)

N,M=map(int,input().split())
A=sorted(list(map(int,input().split())))
bc=sorted([list(map(int,input().split()))for i in range(M)],key=lambda x:x[1],reverse=True)

f=False
pos=0

for b,c in bc:
    for i in range(b):
        if c<=A[pos]:
            f=True
            break
        A[pos]=c
        pos+=1
        if pos==N:
            f=True
            break
    if f:break

print(sum(A))