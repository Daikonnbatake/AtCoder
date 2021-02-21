S=input()
c=0
ans=0
for i in list(S):
    if i=='S':c=0
    else:c+=1
    ans=max(ans,c)
print(ans)