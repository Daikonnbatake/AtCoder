N=int(input())
X=list(map(int,input().split()))
X.sort(key=int)
P=0
out=0
for i in X:
    P+=i
P=round(P/N)

def cost(x,p):
    return (x-p)*(x-p)
for i in X:
    out+=cost(i,P)

print(out)