import bisect

class BinSearch():
    # インスタンス生成時に探索対象(リスト)を渡す
    def __init__(self,l):
        self.l = l
    
    # n の存在を確認
    def is_exist(self,n):
        a = bisect.bisect(self.l,n)
        return self.l[a-1] == n
    
    # n 以下の要素の個数
    def under_n(self,n):
        return bisect.bisect_right(self.l,n)
    
    # n 以上の要素の個数
    def over_n(self,n):
        return len(self.l)-bisect.bisect_left(self.l,n)