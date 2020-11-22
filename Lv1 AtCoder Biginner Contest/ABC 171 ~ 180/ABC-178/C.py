N=int(input())
M=10**9+7
a,b,c=1,1,1
for i in range(N):a,b,c=a*10%M,b*9%M,c*8%M
print((a-b*2+c)%M)