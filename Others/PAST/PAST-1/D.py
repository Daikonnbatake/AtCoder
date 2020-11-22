N=int(input())
s=set()
ok=True
a,b=0,0
for i in range(N):
    A=int(input())
    s.add(A)
    if len(s)!=i+1 and ok==True:
        b=A
        ok=False
s=list(s)
for i in range(1,len(s)+1):
    if s[i-1]>i:
        a=i
        break
if not N in s: a=N
print('Correct' if ok else (str(b)+' '+str(a)))