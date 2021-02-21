N=int(input())
P=list(map(int,input().split()))
mini=(10**5)*2
c=0
for i in range(N):
    if P[i] <= mini:
        mini=P[i]
        c+=1
print(c)