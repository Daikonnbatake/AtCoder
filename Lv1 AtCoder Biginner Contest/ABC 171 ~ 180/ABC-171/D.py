N=int(input())
A=list(map(int,input().split()))
Q=int(input())
L=[0]*(10**5)
S=sum(A)
for i in A:L[i-1]+=1
for i in range(Q):
    B,C=map(int,input().split());B-=1;C-=1
    S+=((C+1)-(B+1))*L[B]
    L[C]+=L[B];L[B]=0
    print(S)