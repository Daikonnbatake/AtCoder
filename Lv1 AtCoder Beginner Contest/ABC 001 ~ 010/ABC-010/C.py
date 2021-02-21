import math
inp=list(map(int,input().split(" ")))
t,T,V,n=[inp[0],inp[1],inp[2],inp[3]],inp[4],inp[5],int(input())
for i in range(n):
    x,y=map(int,input().split(" "))
    value1=math.sqrt((x-t[0])**2+(y-t[1])**2)
    value2=math.sqrt((t[2]-x)**2+(t[3]-y)**2)
    s=value1+value2
    if inp[4]*inp[5] >= s:
        print("YES")
        exit()
print("NO")