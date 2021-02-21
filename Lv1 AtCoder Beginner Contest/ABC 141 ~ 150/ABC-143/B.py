import itertools
N=int,input()
d=itertools.combinations(list(map(int,input().split())),2)
ans=0
for i in d: ans+=i[0]*i[1]
print(ans)