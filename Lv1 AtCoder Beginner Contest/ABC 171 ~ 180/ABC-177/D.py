class Unionfind():
    # 長さ n の自分自身がrootな集合を作る
    def __init__(self,n):
        self.par=[i for i in range(n)]
    # rootを求める
    def root(self,x):
        if self.par[x]==x:return x
        else:return self.root(self.par[x])
    # x と y が同じ集合に属するか否か
    def same(self,x,y):
        return self.root(x)==self.root(y)
    # x と y の属する集合を併合
    def unite(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if self.par[x]>self.par[y]:x,y=y,x
        if x!=y:self.par[x]=y

N,M=map(int,input().split())
f=[i for i in range(N)]
u=Unionfind(N)
c=[0]*N
for i in range(M):
    A,B=map(int,input().split())
    if not u.same(A-1,B-1):u.unite(A-1,B-1)
for i in u.par:c[i]+=1

print(u.par)