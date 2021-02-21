N=int(input())
v=[list(map(int,input().split())) for i in range(N)]
f=False
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and j!=k and i!=k:
                ox,oy=v[i];ox+=1;oy+=1
                ax,ay=v[j];ax+=1;ay+=1
                bx,by=v[k];bx+=1;by+=1
                if (ox-ax)*(oy-by)==(ox-bx)*(oy-ay):f=True
            if f:
                print('Yes')
                exit()
print('No')