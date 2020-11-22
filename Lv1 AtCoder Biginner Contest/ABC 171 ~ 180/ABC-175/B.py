import itertools
N=int(input())
L=list(map(int,input().split()))
ans=0
itr=list(itertools.combinations(L,3))
for i in itr:
    if i[0]!=i[1] and i[1]!=i[2] and i[2]!=i[0]:
        if i[0]+i[1]>i[2]and i[1]+i[2]>i[0]and i[2]+i[0]>i[1]:
            ans+=1
print(ans)