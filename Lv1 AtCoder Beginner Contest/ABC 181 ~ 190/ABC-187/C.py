N=int(input())
s=set()
a=set()

for i in range(N):
    S=input()
    s.add(S)
    a.add(S[1:] if S[0]=='!' else S)

for i in a:
    if '!'+i in s and i in s:
        print(i)
        exit()

print('satisfiable')