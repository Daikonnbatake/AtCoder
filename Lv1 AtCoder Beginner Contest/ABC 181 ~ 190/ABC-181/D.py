import itertools

S = map(int,list(input()))
C = set([i for i in range(1,1000)if i/2%4==0])
num = [0]*10
for i in S:num[i] = min(3,num[i]+1)

s = []
for i in range(10):
    for j in range(num[i]):
        s.append(str(i))
s = itertools.permutations(s,min(3,len(s)))
for i in s:
    n = int(''.join(i))
    if n in C:
        print('Yes')
        exit()
    
print('No')