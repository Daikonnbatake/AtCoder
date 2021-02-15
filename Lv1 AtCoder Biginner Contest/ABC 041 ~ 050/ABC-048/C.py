N,x=map(int,input().split())
A=list(map(int,input().split()))
B=[i for i in A]
if x<B[0]:B[0]=x
for i in range(N-1):
    if x<B[i]+B[i+1]:B[i+1]-=B[i]+B[i+1]-x
print(sum([A[i]-B[i] for i in range(N)]))