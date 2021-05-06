def f(s):
    l,r='',''
    for i in range(len(s)//2):
        l+=s[i]
        r+=s[len(s)-i-1]
    return l==r

N=input()
for i in range(10):
    if f(N):
        print('Yes')
        exit()
    N='0'+N
print('No')