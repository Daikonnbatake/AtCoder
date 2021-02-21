N,S,index = int(input()),[],[]
for i in range(N):
    mem=input()
    if not mem in index :
        index.append(mem)
        S.append(1)
    else:
        S[index.index(mem)]+=1
mem = 0
for i in S:
    if i > mem :
        mem = i
print(index[S.index(mem)])