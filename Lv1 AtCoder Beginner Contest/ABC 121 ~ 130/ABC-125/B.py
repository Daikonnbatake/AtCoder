N=int(input())
V=tuple(map(int,input().split()))
C=tuple(map(int,input().split()))

ans=0

for i in range(1<<N):
    v=0
    c=0
    for j in range(N):
        if i>>j & 1:
            v+=V[j]
            c+=C[j]
    
    ans=max(ans, v-c)

print(ans)