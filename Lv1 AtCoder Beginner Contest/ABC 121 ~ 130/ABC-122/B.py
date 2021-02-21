S=list(input())
ans=0; c=0
for i in range(len(S)):
    if not S[i] in list('AGCT'): c=0
    else:
        c+=1
        ans=max(ans,c)
print(ans)