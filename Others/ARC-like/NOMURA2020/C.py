N=int(input())
A=list(map(int,input().split()))
ans=0
S=2**N #上の階層の葉の最大数
R=0 # 上の階層の枝の最大値
for i in range(N+1):
    d=2**(N-i)
    S=(d//2)-((A[N-(i+1)]+1)//2)
    R=((A[N-(i+1)]+1)//2)
    if A[N-(i+1)] < S:
        print(-1)
        exit()
    ans+=(A[N-(i+1)]+R)
print(ans)