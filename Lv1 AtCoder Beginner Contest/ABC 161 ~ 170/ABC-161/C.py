N,K=map(int,input().split())
print(N%K if N%K < K-(N%K) else K-(N%K))