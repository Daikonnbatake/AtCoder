N,K,S=map(int,input().split())
a=[2 if S==1 else S-1]*N
for i in range(K):a[i]=S
print(' '.join(map(str,a)))