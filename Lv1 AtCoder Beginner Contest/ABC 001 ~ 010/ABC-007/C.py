R,C=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
c=[list(input())for i in range(R)]
V=[[]for i in range(R*C)]
for i in range(R):
    for j in range(C):
        if c[i][j]=='.':
            cu=i*C+j
            if c[i-1][j]=='.':V[cu].append(cu-C);V[cu-C].append(cu)
            if c[i+1][j]=='.':V[cu].append(cu+C);V[cu+C].append(cu)
            if c[i][j-1]=='.':V[cu].append(cu-1);V[cu-1].append(cu)
            if c[i][j+1]=='.':V[cu].append(cu+1);V[cu+1].append(cu)
seen=[-1]*(C*R)
p,q=0,[sy*C+sx-1-C]
seen[q[0]]=0
while len(q)!=p:
    for i in V[q[p]]:
        if seen[i]==-1:
            seen[i]=max(seen[i-1],seen[i+1],seen[i-C],seen[i+C])
            q.append(i)
    p+=1
print(seen[gy*C+gx-1-C])