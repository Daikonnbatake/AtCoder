import bisect

class B():
    def __init__(self,l):self.l = l
    def over_n(self,n):return len(self.l)-bisect.bisect_left(self.l,n)

N=int(input())
A=list(map(int,input().split()))
m=[[]for i in range(200)]
for i in range(N):m[A[i]%200].append(i)
ans=0

for i in range(N):ans+=B(m[A[i]%200]).over_n(i)-1
print(ans)
#[123, 23, 123, 123, 0, 0]