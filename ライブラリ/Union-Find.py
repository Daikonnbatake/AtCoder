class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    #要素 x が属するグループの要素数を返す
    def size(self, x):return -self.parents[self.find(x)]
    #要素 x,y が同じグループに属するかを返す
    def same(self, x, y):return self.find(x) == self.find(y)
    #要素 x が属するグループの要素を返す
    def members(self, x):root = self.find(x);return [i for i in range(self.n) if self.find(i) == root]
    #全ての根の要素をリストで返す
    def roots(self):return [i for i, x in enumerate(self.parents) if x < 0]
    #グループの数を返す
    def group_count(self):return len(self.roots())
    #{root:[そのグループの要素]}を返す
    def all_group_members(self):return {r: self.members(r) for r in self.roots()}
