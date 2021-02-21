N=int(input())
a=[int(input())for i in range(N)]
s=sorted(list(set(a)))
d=dict()
c=0
for i in s:
    d[i]=c
    c+=1

for i in a:print(d[i])