import math
N,A,out=int(input()),list(map(int,input().split(" "))),0
while 0 in A:
    A.remove(0)
for i in A:
    out+=i
print(math.ceil(out/len(A)))