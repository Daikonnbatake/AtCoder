S,T=input(),input()

def check(s,k):
    ok=True
    for i in range(len(s)):
        if s[i]!=k[i] and s[i]!='?':ok=False
    return ok

i,f,m=len(S)-1,True,''
while 0<=i:
    if len(T)<=len(S)-i and check(S[i:i+len(T)],T) and f:f,m=False,T+m[len(T)-1:]
    else:m=('a' if S[i]=='?' else S[i])+m
    i-=1

print('UNRESTORABLE' if f else m)