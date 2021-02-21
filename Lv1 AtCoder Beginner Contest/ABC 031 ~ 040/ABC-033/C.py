S=list(input())
ans=0
m=int(S.pop(0))
for i in range(len(S)//2):
    if S[i*2]=='+':
        if m!=0:
            ans+=1
        m=int(S[i*2+1])
    if S[i*2]=='*':
        m*=int(S[i*2+1])
if m!=0:
    ans+=1
print(ans)