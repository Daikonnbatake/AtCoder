l=list(map(int,input().split()))
for i in range(1<<4):
    a,b=0,0
    for j in range(4):
        if i>>j&1:a+=l[j]
        else:b+=l[j]
    if a==b:print('Yes');exit()
print('No')