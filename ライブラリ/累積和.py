# N,M = map(int,input().split())
# A=list(map(int,input().split()))
# の時、c(N,A)
#出力は長さNの配列
def c(n,array):
    r=[0]*(n+1)
    for i in array:r[i]+=1
    for i in range(1,n+1):r[i]+=r[i-1]
    return(r)