import math
N,D=map(int,input().split())
ans=0
pos=[]
for i in range(N): pos.append(list(map(int,input().split())))
for i in range(N):
    y=pos[i]
    for j in range(N):
        z=pos[j]
        if i==j: pass
        else:
            distance=0.0
            for k in range(D): distance+=(y[k]-z[k])**2
            if math.sqrt(distance).is_integer(): ans+=1
print(ans//2)