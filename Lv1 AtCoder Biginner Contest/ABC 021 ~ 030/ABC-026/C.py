N=int(input())
l=[[0]*N for i in range(N)]

for i in range(N-1):
    B=int(input())
    l[B-1][i+1]+=1
m=[0]*N
for i in range(N):
    mem=[]
    for j in range(N):
        if l[N-i-1][j]:
            mem.append(m[j])
    if 0<len(mem):m[N-i-1]=max(mem)+min(mem)+1
    else:m[N-i-1]=1
ans=[]
for i in range(N):
    if l[0][i]:ans.append(m[i])
print(max(ans)+min(ans)+1)