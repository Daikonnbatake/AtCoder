N=int(input())
C=[['']*N for i in range(N)]
l,r='',''
char=list('abcdefghijklmnopqrstuvwxyz')
for i in range(N): C[i]=list(input())
for i in range(N//2):
    ok=True
    c=''
    for j in char:
        if (j in C[i]) and (j in C[len(C)-(i+1)]):
            c=j
            break
        if j=='z': ok=False
    if ok==False:
        print(-1)
        exit()
    l=l+c; r=c+r
print(l+r if N%2==0 else l+C[(N//2)][0]+r)