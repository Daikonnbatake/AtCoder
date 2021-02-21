N=int(input())
c=list(input())
m=c.count('R')
a=0
for i in range(m):
    if c[i]=='R':
        a+=1
print(m-a)