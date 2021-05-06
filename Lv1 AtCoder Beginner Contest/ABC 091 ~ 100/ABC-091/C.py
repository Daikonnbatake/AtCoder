N=int(input())
R=[tuple(map(int,input().split())) for i in range(N)]
B=[tuple(map(int,input().split())) for i in range(N)]
R.sort(key=lambda x:sum(x)**0.5)
B.sort(key=lambda x:sum(x)**0.5)
m=[1]*N
for a,b in R:
    for i in range(N):
        c,d=B[i]
        if a<c and b<d and m[i]:
            m[i]=0
            break
print(m.count(0))