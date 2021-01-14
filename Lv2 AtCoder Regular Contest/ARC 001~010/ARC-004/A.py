import math
N=int(input())
pos=[list(map(int,input().split()))for i in range(N)]
 
ans=0
 
for i in range(N):
    for j in range(i+1,N):
        ans = max(ans,math.sqrt((pos[i][0]-pos[j][0])**2 + (pos[i][1]-pos[j][1])**2))
 
print(ans)