N=int(input())
A=list(map(int,input().split()))
ans=['']*N
for i in range(N): ans[A[i]-1]=str(i+1)
print(' '.join(ans))