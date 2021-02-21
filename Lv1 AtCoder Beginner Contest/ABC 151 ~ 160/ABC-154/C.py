N,A=int(input()),list(map(int,input().split()))
A=sorted(A,key=int)
l=set([])
for i in A:
    if i in l:
        print("NO")
        exit()
    else:
        l.add(i)
print("YES")