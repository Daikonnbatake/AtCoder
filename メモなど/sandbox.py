import bisect
class BinSearch():
    def __init__(self,l):self.l = l
    def over_n(self,n):return bisect.bisect_left(self.l,n)
N,S=int(input()),input()
p=[[]for i in range(10)]
ans=0
for i in range(N):p[int(S[i])].append(i)
for i in range(1000):
    a=0
    ok=True
    for j in map(int,list(str(i).zfill(3))):
        b=BinSearch(p[j])
        if len(p[j])-b.over_n(a)==0:ok=False;break
        a=p[j][b.over_n(a)]+1
    if ok:ans+=1
print(ans)