H,W=map(int,input().split())
S=[list(input())for i in range(H)]

ans=0
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            if S[i-1][j]=='.' and S[i][j-1]=='.':ans+=1
            if S[i-1][j]=='.' and S[i][j+1]=='.':ans+=1
            if S[i+1][j]=='.' and S[i][j-1]=='.':ans+=1
            if S[i+1][j]=='.' and S[i][j+1]=='.':ans+=1

            if S[i-1][j]=='#' and S[i][j-1]=='#' and S[i-1][j-1]=='.':ans+=1
            if S[i-1][j]=='#' and S[i][j+1]=='#' and S[i-1][j+1]=='.':ans+=1
            if S[i+1][j]=='#' and S[i][j-1]=='#' and S[i+1][j-1]=='.':ans+=1
            if S[i+1][j]=='#' and S[i][j+1]=='#' and S[i+1][j+1]=='.':ans+=1

print(ans)