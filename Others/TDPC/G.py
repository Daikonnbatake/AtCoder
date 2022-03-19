import math
def C(n,r):return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)

c=[0]*26
for i in list(input()): c[ord(i)-97]+=1
N,M=sum(c),26-c.count(0) 
K=int(input())

dp=[[0]*N for i in range(M)]

for i in range(N):
    for j in range(M):
