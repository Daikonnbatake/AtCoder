n,X=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
count=0
for i in range(n):
    if X>>i & 1:
        count+=a[i]
print(count)