H,W,K=map(int,input().split())
c=[input() for i in range(H)]

ans=0
for h in range(1<<H):
    for w in range(1<<W):
        count=0
        for i in range(H):
            for j in range(W):
                if (h>>i)&1 and (w>>j)&1:
                    if c[i][j]=='#':count+=1
        if count==K:ans+=1
print(ans)