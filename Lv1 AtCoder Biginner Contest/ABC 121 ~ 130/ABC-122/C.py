N,Q=map(int,input().split())
S=list(input()+'T')
index=[0]*(N+1); s=0
for i in range(1,N+1):
    if S[i-1]+S[i]=='AC': s+=1
    index[i]=s
for i in range(Q):
    l,r=map(int,input().split())
    if S[l-1]=='C': print(index[r-1]-index[l])
    else: print(index[r-1]-index[l-1])