import math
N=int(input())
R=sorted([int(input())**2 for i in range(N)])
ans=0
for i in range(N):
    if (N-i-1)%2:ans-=R[N-i-1]
    else:ans+=R[N-i-1]
print(abs(ans*math.pi))