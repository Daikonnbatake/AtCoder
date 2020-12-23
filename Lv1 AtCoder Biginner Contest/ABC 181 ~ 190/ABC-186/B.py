H,W=map(int,input().split())
A=[]
for i in range(H):A.extend(map(int,input().split()))
MIN=min(A)
ans=0
for i in A:ans+=i-MIN
print(ans)