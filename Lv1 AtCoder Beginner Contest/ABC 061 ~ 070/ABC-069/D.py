H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))
mag=[i+1 for i in range(N) for j in range(a[i])]
ans=[[0]*W for i in range(H)]

for i in range(H):
    for j in range(W):
        if i%2:ans[i][W-j-1]=mag[i*W+j]
        else: ans[i][j]=mag[i*W+j]

for i in ans:print(' '.join(map(str,i)))