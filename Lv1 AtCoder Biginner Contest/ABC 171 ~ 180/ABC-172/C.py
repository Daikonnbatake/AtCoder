import bisect
class BinSearch():
    def __init__(self,l):self.l = l
    def is_exist(self,n):a = bisect.bisect(self.l,n);return self.l[a-1] == n
    def under_n(self,n):return bisect.bisect_right(self.l,n)
    def over_n(self,n):return len(self.l)-bisect.bisect_left(self.l,n)

N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a,b=[0]*(N+1),[0]*(M+1)
for i in range(N):a[i+1]=A[i]+a[i]
for i in range(M):b[i+1]=B[i]+b[i]
bb=BinSearch(b)
ans=0
for i in range(N+1):
    if a[i]<=K:
        j=max(0,bb.under_n(K-a[i])-1)
        ans=max(ans,i+j)
print(ans)