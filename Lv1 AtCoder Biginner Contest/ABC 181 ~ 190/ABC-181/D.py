import itertools
S=input()
N=int(S)
c=[0]*9
for i in list(S):c[int(i)-1]+=1

if len(S)<4:
    s=list(itertools.permutations(list(S)))
    for i in s:
        if int(''.join(i))%8==0:
            print('Yes')
            exit()
else:
    m=96
    while m<1000:
        d=[0]*9
        m+=8
        for i in list(str(m)):d[int(i)-1]+=1
        f=True
        for i in range(9):
            if c[i]<d[i]:f=False
        if f:
            print('Yes')
            exit()
print('No')