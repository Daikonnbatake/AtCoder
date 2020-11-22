N,K=map(int,input().split())
p=list(map(int,input().split()))
p.sort(key=int)
print(sum(p[0:K]))