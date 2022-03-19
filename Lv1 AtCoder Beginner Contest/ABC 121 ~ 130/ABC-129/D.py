H,W=map(int,input().split())
S=[list(input()) for i in range(H)]

hc=0
hm=dict()
hl=[[0]*W for i in range(H)]
ans=0

for h in range(H):
    hc+=1
    hm[hc]=0
    for w in range(W):
        if S[h][w]=='#':
            hc+=1
            hm[hc]=0
            continue
        hl[h][w]=hc
        hm[hc]+=1

for w in range(W):
    m=0
    wc=0
    for h in range(H):
        if S[h][w]=='#':
            m=0
            wc=0
            continue
        m=max(m,hm[hl[h][w]])
        ans=max(ans,m+wc)
        wc+=1

print(ans)