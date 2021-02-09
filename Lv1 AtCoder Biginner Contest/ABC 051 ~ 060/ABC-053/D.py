N=int(input())
A=list(map(int,input().split()))

a=[0]*10**5
for i in A:a[i-1]+=1

card=0
for i in a:
    if 1<i:card += i-1
card += 1 if card%2 else 0
print(N-card)