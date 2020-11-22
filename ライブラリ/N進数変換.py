#10進数の数値と底を入力すると進数変換(10進数のタプルを返す)が出来る
#任意の引数kに数値を入れるとmin(k,len(r))の桁数で0埋めする
def nn(n,x,k=-1):
    m=n;r=[]
    while 0<m:
        r.insert(0,m%x)
        m=m//x
    while len(r)<k:r.insert(0,0)
    return r