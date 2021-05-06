H,W,X,Y=map(int,input().split())
S=[list(input())for i in range(H)]
h,w=[],[]
ans=1

for i in range(H):h.append(S[i][Y-1])
for i in range(W):w.append(S[X-1][i])

for i in range(X,H):
    if h[i]=='#':break
    ans+=1

for i in range(X-1):
    i=X-i-2
    if h[i]=='#':break
    ans+=1

for i in range(Y,W):
    if w[i]=='#':break
    ans+=1

for i in range(Y-1):
    i=Y-i-2
    if w[i]=='#':break
    ans+=1

print(ans)