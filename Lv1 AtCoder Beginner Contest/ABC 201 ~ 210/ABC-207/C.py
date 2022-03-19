N=int(input())
tlr=[list(map(int,input().split())) for i in range(N)]
s=set()
d=dict()
for t,l,r in tlr: s.add(l); s.add(r)
ss=sorted(list(s))
for i in range(len(ss)):d[ss[i]]=i+1
S=[0]*(len(ss)+1)

for i in range(N):
    t,l,r=tlr[i]
    l,r=d[l],d[r]
    if t==1:l,r=l-1,r
    if t==2:l,r=l-1,r-1
    if t==3:l,r=l,r
    if t==4:l,r=l,r-1
    S[l]+=1
    S[r]-=1

ans=0
for i in range(1,len(ss)):
    S[i]+=S[i-1]
    ans+=S[i]-1

print(ans+1 if ans else 0)