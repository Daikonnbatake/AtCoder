N=int(input())
l=[8,4,2,1]
a=[]
while True:
    if sum(a) == N:
        break
    for i in range(4):
        if l[i]+sum(a) <= N:
            a.append(l[i])
print(len(a))
for i in a: print(i)