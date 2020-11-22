N,M=map(int,input().split())
ac=[0]*N
wa=[0]*N
pena=0
acsum=0
for i in range(M):
    p,S=input().split()
    p=int(p)-1
    if S == 'AC':
        if ac[p]==0:
            ac[p]=1
            pena+=wa[p]
            acsum+=1
    else:
        wa[p]+=1
print(acsum,pena)