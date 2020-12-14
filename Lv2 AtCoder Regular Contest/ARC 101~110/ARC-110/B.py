N=int(input())
T=list(input())
if N==1:
    if T==['0']:print(10**10)
    else:print((10**10)*2)
elif N==2:
    if T==['0','1']:print(10**10-1)
    if T==['1','0']:print(10**10)
    if T==['1','1']:print(10**10)
    if T==['0','0']:print(0)
else:
    if ''.join(T[:3]) in ['110','101','011'] and ''.join(T[-3:]) in ['110','101','011']:
        a={'110':0,'101':1,'011':2}[''.join(T[:3])]
        m=[a,{'110':0,'101':2,'011':1}[''.join(T[-3:])]]
        check=True
        for i in range(N):
            if T[i]!=['1','1','0'][a]:check=False
            a=(a+1)%3
        if check:
            b=10**10*3-N+3-sum(m)
            print(b//3)
        else:
            print(0)
    else:print(0)