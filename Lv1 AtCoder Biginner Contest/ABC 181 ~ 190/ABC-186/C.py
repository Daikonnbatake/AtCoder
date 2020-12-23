def nn(n,x):
    m=n;r=[]
    while 0<m:
        r.insert(0,m%x)
        m=m//x
    return r

N=int(input())
a=set()

for i in range(N+1):
    if '7' in str(i):a.add(i)

for i in range(N+1):
    if 7 in nn(i,8):a.add(i)

print(N-len(a))