N,K,M = map(int,input().split(" "))
A = map(int,input().split(" "))
mem = 0
for i in A :
    mem = mem + i
if (mem + K)/N < M :
    i = -1
else:
    Ab = mem
    i = 0
if i == 0:
    while Ab/N < M:
        i  = i+1
        Ab = mem + i
print(i)