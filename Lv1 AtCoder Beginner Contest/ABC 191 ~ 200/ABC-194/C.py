import itertools as itr
N=int(input())
A=list(map(int,input().split()))
a=[0]*401
ans=0
for i in A:a[i+200]+=1
for i,j in itr.combinations(range(401),2):
    ans+=(a[i]-a[j])