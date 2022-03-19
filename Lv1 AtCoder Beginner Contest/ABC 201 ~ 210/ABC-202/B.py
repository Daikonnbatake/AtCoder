S=list(input())
ans=''
for i in S:
    if int(i)==6:ans+='9'
    elif int(i)==9:ans+='6'
    else:ans+=i
print(''.join([ans[len(ans)-i-1] for i in range(len(ans))]))