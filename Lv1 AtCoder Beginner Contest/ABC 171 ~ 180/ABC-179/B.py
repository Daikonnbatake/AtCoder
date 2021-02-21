N=int(input())
z=0
ans=0
for i in range(N):
    a,b=map(int,input().split())
    if a==b:z+=1
    else:
        ans=max(ans,z);z=0
ans=max(ans,z)
print('Yes'if 2<ans else'No')