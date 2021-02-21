N=int(input())
data=[]
for i in range(N):
    d=list(input().split())
    d[1]=int(d[1])
    d.append(i+1)
    data.append(d)
data.sort()
mem=[]; current=''
ans=[]
for i in data:
    if current!=i[0]:
        current=i[0]
        mem.sort(key=lambda x:x[1])
        d=[0]*len(mem)
        for j in range(len(mem)): d[len(mem)-(j+1)]=mem[j][2]
        ans.extend(d)
        mem=[i]
    else: mem.append(i)
mem.sort(key=lambda x:x[1])
d=[0]*len(mem)
for j in range(len(mem)): d[len(mem)-(j+1)]=mem[j][2]
ans.extend(d)
mem=[i]
for i in ans: print(i)