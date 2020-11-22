a=list(map(int,input().split()))
c5,c7=0,0
for i in a:
    if i==5:
        c5+=1
    elif i==7:
        c7+=1
print("YES" if(c5==2  and c7==1) else "NO")