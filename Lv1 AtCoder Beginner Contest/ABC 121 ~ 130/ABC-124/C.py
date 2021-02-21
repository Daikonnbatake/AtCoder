S=list(input())
ans=0
for i in range(1,len(S)):
    if S[i-1]==S[i]: ans+=1; S[i]= '0' if S[i]=='1' else '1'
print(ans)