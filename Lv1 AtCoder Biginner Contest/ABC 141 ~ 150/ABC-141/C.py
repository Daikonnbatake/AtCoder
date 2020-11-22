N,K,Q=map(int,input().split())
score=[0]*N
for i in range(Q):
    A=int(input())-1
    score[A]+=1
for i in score:
    if Q-K < i: print('Yes')
    else: print('No')