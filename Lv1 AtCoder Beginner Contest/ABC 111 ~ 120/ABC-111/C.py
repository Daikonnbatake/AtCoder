def mode(l):
    r=dict()
    for i in l:
        if i in r: r[i]+=1
        else: r[i]=1
    r=list(r.items())
    return [i for i,j in sorted(r,key=lambda x:x[1])]

N=int(input())
ans=0

o,e=[],[]
for i in map(int,input().split()):
    if len(o)==len(e): o.append(i)
    else: e.append(i)

os,es=set(o),set(e)

if len(os)==1 and len(es)==1:
    if os==es: ans=N//2
else:
    mo=mode(o)[-2:]
    me=mode(e)[-2:]
    if mo[-1]!=me[-1]:
        ans=N//2-o.count(mo[-1]) + N//2-e.count(me[-1])
    else:
        A=N//2-o.count(mo[-1])+N//2-e.count(me[-2]) if len(me)==2 else 10**6
        B=N//2-o.count(mo[-2])+N//2-e.count(me[-1]) if len(mo)==2 else 10**6
        ans=min(A,B)
print(ans)