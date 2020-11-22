N,M=map(int,input().split())
D=[]
ans=0; count=0
for i in range(N): 
    A,B=map(int,input().split())
    D.append([A,B])
D.sort()
for i in range(N):
    if count==M: break
    if D[i][1]+count<=M:
        count+=D[i][1]
        ans+=D[i][0]*D[i][1]
    else:
        ans+=D[i][0]*(M-count)
        count=M
print(ans)