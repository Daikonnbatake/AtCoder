A,B,X=map(int,input().split())
def f(n): return (A*n)+(B*len(str(n)))

l,r=0,10**9
while l <= r:
    m = (l+r)//2
    if X < f(m): r=m-1
    if X > f(m): l=m+1

    print(m)