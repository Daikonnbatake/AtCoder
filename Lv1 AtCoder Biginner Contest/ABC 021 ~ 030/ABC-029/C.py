def t(n):
    r=''
    m=n
    while m:
        r=['a','b','c'][m%3]+r
        m=int(m/3)
    if n==0:r='a'
    while len(r)<N:
        r='a'+r
    return r

N=int(input())

for i in range(3**N):
    print(t(i))