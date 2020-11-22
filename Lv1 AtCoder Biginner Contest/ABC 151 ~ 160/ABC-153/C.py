N,K = map(int,input().split(" "))
l = list(map(int,input().split(" ")))
H = sorted(l,key=int) 
c = 0
if(K >= N):
    c = 0
else:
    for i in range(K):
        del H[-1]
    for i in H:
        c = c+i
print(c)