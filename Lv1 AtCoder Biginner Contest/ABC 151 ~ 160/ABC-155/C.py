N=int(input())
data={}
for i in range(N):
    name=input()
    if data.get(name) == None:
        data[name]=0
    data[name] += 1
data = sorted(data.items(),key=lambda x:x[1])
if len(data) == 1:
    print(data[-1][0])
else:
    mx=data[-1][1]
    l=[]
    for i in range(N):
        if data[len(data)-i-1][1] == mx:
            l.append(data[len(data)-i-1][0])
        else:
            break
    l.sort()
    for i in l: print(i)