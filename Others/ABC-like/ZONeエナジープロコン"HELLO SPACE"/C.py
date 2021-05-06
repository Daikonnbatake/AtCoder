N=int(input())
l=[list(map(int,input().split())) for i in range(N)]
m=sorted([[min(l[i]),i] for i in range(N)],key=lambda x: x[0])
ans=0

# i番目とj番目の人を決めて能力値のminが一番大きい人を選ぶ

for i in range(N):
    for j in range(i+1,N):
        for k in range(N):
            k=N-k-1
            if not m[k] in [i,j]:break
        a=max(l[i][0],l[j][0],l[m[k][1]][0])
        b=max(l[i][1],l[j][1],l[m[k][1]][1])
        c=max(l[i][2],l[j][2],l[m[k][1]][2])
        d=max(l[i][3],l[j][3],l[m[k][1]][3])
        e=max(l[i][4],l[j][4],l[m[k][1]][4])
        ans=max(ans,min(a,b,c,d,e))
print(ans)