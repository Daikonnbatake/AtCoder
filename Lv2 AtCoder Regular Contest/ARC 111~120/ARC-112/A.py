def rsum(n):return(n+1)*(n//2)+(n+1)//2 if n%2 else(n+1)*(n//2)
def q(L,R):return rsum(R-L-1)

for i in range(int(input())):
    L,R=map(int,input().split())
    print(q(L,R))