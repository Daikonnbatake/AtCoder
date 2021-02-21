S=input()
T=input()
ans=len(T)
for i in range(len(S)-len(T)+1):
    s=S[i:i+len(T)+1]
    m=0
    for j in range(len(T)):
        if s[j]!=T[j]:
            m+=1
    ans=min(ans,m)
print(ans)