s=list(input())
ans=[]
m=0;c=s[0]
for i in range(len(s)):
    if c!=s[i]: ans.extend([c,str(m)]); c=s[i]; m=1
    else: m+=1
ans.extend([c,str(m)])
print(''.join(ans))