D,G=map(int,input().split())
P,C=[0]*D,[0]*D
for i in range(D):P[i],C[i]=map(int,input().split())
ans=10**9
for i in range(1,1<<D):
    A,g,m=[],0,0
    for j in range(D):
        if i>>j&1:A.append([P[j],C[j],100*(j+1)])
    for j in range(len(A)):
        j=len(A)-j-1
        a,b,c=A[j][2],A[j][1],A[j][0]
        if G<=g+(a*(c-1)):ans=min(ans,-(-(G-g)//a)+m);break
        elif G<=g+(a*c)+b:ans=min(ans,c+m);break
        g+=(a*c)+b;m+=c
print(ans)