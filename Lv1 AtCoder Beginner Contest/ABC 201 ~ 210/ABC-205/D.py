N,Q=map(int,input().split())
A=list(map(int,input().split()))
posMap={i:e for i,e in enumerate(sorted(A))}

def binS(K):
    if K<A[0]:return 0
    ng = 0
    ok = N-1
    while ok-ng>1:
        mid = (ok+ng)//2
        if posMap[mid] <= K: ng = mid
        else: ok = mid
    
    return ok

for q in range(Q):
    K = int(input())
    print(binS(K)+K)