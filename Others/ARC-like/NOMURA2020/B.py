T=list(input())
S=['']*len(T)
for i in range(len(T)):
    if T[i] in ['D','P']: S[i]=T[i]
    else: S[i]='D'
print(''.join(S))