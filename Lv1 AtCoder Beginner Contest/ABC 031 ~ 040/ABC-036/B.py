N=int(input())
S=[list(input())for i in range(N)]
A=[['']*N for i in range(N)]
for i in range(N):
    for j in range(N):
        A[j][N-i-1]=S[i][j]
for i in A:print(''.join(i))