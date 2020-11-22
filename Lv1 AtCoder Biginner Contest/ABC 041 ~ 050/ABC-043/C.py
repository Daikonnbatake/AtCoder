N=int(input())
a=list(map(int,input().split()))

def rewrite(n,l):
    cost=0
    for i in l:
        cost += (i-n)**2
    return cost

r1=rewrite(int(sum(a)/len(a)),a)
r2=rewrite(int(sum(a)/len(a))+1,a)

print(r1 if r1<r2 else r2)