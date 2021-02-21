a,b=map(int,input().split())
l=["",""]
for i in range(b):
    l[0]=l[0]+str(a)
for i in range(a):
    l[1]=l[1]+str(b)
l.sort()
print(l[0])