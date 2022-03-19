S=input()
ans=0
C=S.count('o')
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                ok=True
                A=[S[a],S[b],S[c],S[d]]
                if 'x' in A:ok = False
                if len(set([[a,b,c,d][i]for i in range(4) if A[i]=='o']))<C:ok=False
                
                if ok:
                    ans+=1
print(ans)