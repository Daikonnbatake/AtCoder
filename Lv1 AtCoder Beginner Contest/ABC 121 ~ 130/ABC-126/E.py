N,M=map(int,input().split())
xyz=[]
for x,y,z in tuple(map(int,input().split()) for i in range(M)): xyz.append([x, y, z%2])
A=[0]*N
inf=10**10

# Mから知ることのできるカードを網羅した後に、知ることが出来なかったカードのコストを支払う

for x,y,z in xyz:
    if z:
        if A[x-1]:
        A[x-1], A[y-1] = -y, -x

    else:
        if A[x-1] or A[y-1]:continue
        A[x-1], A[y-1] = y, x

print(A)