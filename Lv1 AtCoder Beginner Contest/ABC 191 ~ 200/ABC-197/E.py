import bisect
class BinSearch():
    def __init__(self,l):self.l = l
    # n の存在を確認
    def is_exist(self,n):
        a = bisect.bisect(self.l,n)
        return self.l[a-1] == n
    # n 以下の要素の個数
    def under_n(self,n):return bisect.bisect_right(self.l,n)
    # n 以上の要素の個数
    def over_n(self,n):return len(self.l)-bisect.bisect_left(self.l,n)

N=int(input())
xc=[tuple(map(int,input().split())) for i in range(N)]
xc.sort(key=lambda x:x[1])
d=dict()
seen=
for x,c in xc:
    if c in d: d[c].append(x)
    else:d[c]=[x]

for i in d:


print(d)