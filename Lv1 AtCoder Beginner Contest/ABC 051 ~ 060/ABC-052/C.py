def f(n):
    arr=[];temp=n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1: arr.append([temp, 1])
    if arr==[]: arr.append([n, 1])
    return arr

N=int(input())
d=dict()
ans=1

for i in range(N):
    for a,b in f(i+1):
        if a in d: d[a]+=b
        else: d[a]=b

for k,v in d.items():
    if k!=1:ans *= v+1

print(ans%1000000007)