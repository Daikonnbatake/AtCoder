N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=A.pop(-1)
if 0 in A:
    print(0)
else:
    for i in range(N-1):
        ans=ans*A[N-(i+2)]
        if ans > (10**18): break
        if ans == 0: break
    print(ans if ans<=10**18 else -1)