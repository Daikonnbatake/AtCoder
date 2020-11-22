N=int(input())
S,P=[0]*N,[0]*N
for i in range(N):S[i],P[i]=input().split();P[i]=int(P[i])
for i in range(N):
    if sum(P)/2<P[i]:print(S[i]);exit()
print('atcoder')