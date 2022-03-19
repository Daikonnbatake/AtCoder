A,B,C=map(int,input().split())

if C%2==0:
    if A<0: A=abs(A)
    if B<0: B=abs(B)

if A==B:print('=')
else:print('<' if A<B else '>')