N,S=input().split()
N=int(N)
at,cg='',''
for i in range(N):
    if S[i]in['A','T']:at+=S[i]
    else:cg+=S[i]
l=list(at)
s=at[0]
for i in range(1,len(at)):
    if 