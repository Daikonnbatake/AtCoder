H,W=map(int,input().split())
C=list(map(int,input().split()))
D=C=list(map(int,input().split()))
M=[list(input())for i in range(H)]
X,Y=[[0]*W for i in range(H-1)],[[0]*H for i in range(W-1)]

x,y=0,0
for i in range(H-1):
    s=0
    for j in range(W):
        if M[i][j]=='#' or M[i+1][j]=='#':
            X[i][j]=1
            s+=1
    if s==W:x+=1

for i in range(W-1):
    s=0
    for j in range(H):
        if M[j][i]=='#' or M[j][i+1]=='#':
            Y[i][j]=1
            s+=1
    if s==H:y+=1

print(max(x,y))