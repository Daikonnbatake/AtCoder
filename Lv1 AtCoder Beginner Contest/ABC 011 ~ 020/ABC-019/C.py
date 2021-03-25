def f(n):
    ret=n
    while ret%2==0:ret//=2
    return ret
N=int(input())
s=set()
for i in input().split():s.add(f(int(i)))
print(len(s))