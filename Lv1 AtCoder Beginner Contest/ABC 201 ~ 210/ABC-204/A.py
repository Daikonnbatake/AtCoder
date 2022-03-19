x,y=map(int,input().split())

if x==y: print(x)
else:
    a=[0,1,2]
    a.pop(a.index(x))
    a.pop(a.index(y))
    print(a[0])