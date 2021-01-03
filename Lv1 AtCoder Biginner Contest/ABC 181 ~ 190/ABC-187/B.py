N=int(input())

pos=[list(map(int,input().split())) for i in range(N)]

ans=0

for i in range(N):
    for j in range(i+1,N):
        Ax,Ay=pos[i]
        Bx,By=pos[j]
        Bx-=Ax;By-=Ay
        if abs(By/Bx)<=1:
            ans+=1

print(ans)