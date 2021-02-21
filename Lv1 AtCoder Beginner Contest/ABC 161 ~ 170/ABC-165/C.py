import itertools as itr

N,M,Q=map(int,input().split())
abcd=[list(map(int,input().split()))for i in range(Q)]
ans=0

for i in itr.combinations_with_replacement(list(range(1,M+1)),N):
    m=0
    for a,b,c,d in abcd:
        if i[b-1]-i[a-1]==c:m+=d
    ans=max(ans,m)

print(ans)