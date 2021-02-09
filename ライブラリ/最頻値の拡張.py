# 個数が少ない→多い順にソートして出力
def mode(l):
    r=dict()
    for i in l:
        if i in r: r[i]+=1
        else: r[i]=1
    r=list(r.items())
    return [i for i,j in sorted(r,key=lambda x:x[1])]