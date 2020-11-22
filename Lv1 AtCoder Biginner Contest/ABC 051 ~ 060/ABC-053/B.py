s=list(input())
l,r=0,len(s)
for i in range(len(s)):
    if s[i]=='A':l=i;break
for i in range(len(s)):
    if s[len(s)-(i+1)]=='Z':r=len(s)-(i+1);break
print(r-l+1)