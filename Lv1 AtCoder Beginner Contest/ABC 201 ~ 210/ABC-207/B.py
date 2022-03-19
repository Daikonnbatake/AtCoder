A,B,C,D=map(int,input().split())

b,r=0,0
c=0
while A+b > r*D:
    c+=1
    b+=B
    r+=C
    if c==10**6:
        print(-1)
        exit()
print(c)