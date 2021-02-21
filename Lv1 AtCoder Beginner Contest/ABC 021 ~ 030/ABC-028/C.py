import itertools
l=list(map(int,input().split()))
m=list(itertools.combinations(l,3))
a=[0]*len(m)
for i in range(len(m)):a[i]=sum(m[i])
a.sort()
print(a[-3])