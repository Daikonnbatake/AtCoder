r,D,x=map(int,input().split())
ans=0
for i in range(10):
    i+=2000
    print(r*x-D)
    x=r*x-D