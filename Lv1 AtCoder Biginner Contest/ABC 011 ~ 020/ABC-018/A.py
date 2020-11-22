a=[int(input()) for i in range(3)]
l=sorted(a)[::-1]
for i in a:
    print(1+l.index(i))