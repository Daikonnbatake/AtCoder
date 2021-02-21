a,b=input().split()
A,B=0,0
for i in list(a):A+=int(i)
for i in list(b):B+=int(i)
print(max(A,B))