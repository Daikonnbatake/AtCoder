N,S=int(input()),list(input())
ans=0
c=1
while c<N:
    if S[c]!=S[c-1]: ans+=1
    c+=1
print(ans+1)