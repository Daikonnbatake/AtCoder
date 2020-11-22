K,N=map(int,input().split())
A=list(map(int,input().split()))
R=[]
for i in range(N):
    if i == N-1:
        R.append(abs(A[i]-(K+A[0])))
    else:
        R.append(abs(A[i]-A[i+1]))
R.sort(key=int)
print(K-R.pop(-1))