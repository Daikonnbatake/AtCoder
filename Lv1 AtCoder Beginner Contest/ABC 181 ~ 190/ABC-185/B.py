N,M,T=map(int,input().split())
ans=True
t=0
for i in range(M):
    A,B=map(int,input().split())
    N-=A-t
    if N<=0:ans=False
    print(N)
    N+=B-A-1
    t=B
print('Yes'if ans else 'No')