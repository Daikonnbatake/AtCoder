S=input()
ok=True
c=list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(S)):
    if i%2:
        if S[i] in c:ok=False
    else:
        if not S[i] in c:ok=False

print('YNeos'[not ok::2])