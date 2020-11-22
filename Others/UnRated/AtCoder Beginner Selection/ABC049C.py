S = input()
N = len(S)
s = set(['dream', 'dreamer', 'erase', 'eraser'])

mem = ''
flag = True
for i in range(N):
    if mem in s:
        mem = S[N-i-1]

    else:
        mem = S[N-i-1] + mem
    
    if 7<len(mem):
        flag = False

if not mem in s or mem == '':
    flag = False

if flag == True:
    print('YES')

else:
    print('NO')