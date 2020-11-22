N,M=map(int,input().split())
H=list(map(int,input().split()))
l=[1]*N
for i in range(M):
    A,B=map(int,input().split())
    A-=1
    B-=1
    if H[A] <= H[B]:
        l[A] = 0
    if H[A] >= H[B]:
        l[B] = 0
print(l.count(1))