N,S,Q=int(input()),list(input()),int(input())
flag=0
for i in range(Q):
    T,A,B=map(int,input().split())
    if T==2:
        if flag:flag=0
        else:flag=1
    else:
        if flag:
            a=N+A-1 if A<=N else A-N-1
            b=N+B-1 if B<=N else B-N-1
            S[a],S[b]=S[b],S[a]
        else:
            S[A-1],S[B-1]=S[B-1],S[A-1]
if flag:S=S[N:]+S[:N]
print(''.join(S))