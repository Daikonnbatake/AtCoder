N,K=map(int,input().split())
S=input()
print((S[:K-1]if 0<=K-2 else '')+S[K-1].lower()+S[K:])