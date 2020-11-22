N=int(input())
a=list(map(int,input().split()))
a.insert(0,a[-1])
a.append(a[1])
for i in range(1,N+1):
    if a[i-1]^a[i+1]!=a[i]:
        print('No')
        exit()
print('Yes')