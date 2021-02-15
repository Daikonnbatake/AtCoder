import itertools as itr

N,K=map(int,input().split())
T=[list(map(int,input().split()))for i in range(N)]
p=itr.product([i+1 for i in range(K)],repeat=N)
ok=True

for i in p:
    m = T[0][i[0]-1]
    for j in range(1,N): m ^= T[j][i[j]-1]
    if m==0: ok=False

print('Nothing' if ok else 'Found')