N=int(input())
A=sorted(list(map(int,input().split())))
mod=10**9+7
ok=True
for i in range(N//2):
    if A[N-i*2-1]!=A[N-i*2-2]:ok=False

print(pow(2,N//2,mod) if ok else 0)