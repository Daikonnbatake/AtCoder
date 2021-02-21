import itertools
S,N=list(input()),int(input())
A=[]
for i in range(len(S)):
    for j in range(len(S)):
        A.append(S[i]+S[j])
print(A[N-1])