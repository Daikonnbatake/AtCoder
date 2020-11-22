N=int(input())
p=list(map(int,input().split()))
now=0
s=set()
for i in p:
    s.add(i)
    if now==i:
        while now in s:now+=1
    print(now)