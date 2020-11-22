S=list(input())
ans=True
for i in range(len(S)):
    if (i+1)%2==0 and S[i]=='R': ans=False
    elif (i+1)%2==1 and S[i]=='L': ans=False
print('Yes' if ans else 'No')