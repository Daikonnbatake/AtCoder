def nn(n,x,k=-1):
    m=n;r=[]
    while 0<m:
        r.insert(0,m%x)
        m=m//x
    return r
N=int(input())
a=[]
ans=0
for i in range(1,3**10):
    m=nn(i,3)[1:]
    s=''
    if 0 in m and 1 in m and 2 in m:
        for j in range(len(m)):s+=['3','5','7'][m[j]]
        s=int(s)
        if 356<s:a.append(s)
a=sorted(list(set(a)))
for i in a:
    if N<i:break
    ans+=1
print(ans)