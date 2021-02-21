N=int(input())
A=list(map(int,input().split()))

def f(l):
    r = []
    for i in range(len(l)//2): r.append(max(l[2*i+1],l[2*i]))
    return r

b = A

for i in range(N-1):
    a = f(b)
    b = a

print(A.index(min(b))+1)