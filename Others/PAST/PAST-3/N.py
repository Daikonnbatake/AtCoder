
N,Q=map(int,input().split())
a=list(range(1,N+1))
for i in range(Q):
    t,x,y=map(int,input().split())
    
    #クエリ1
    if t==1: a[x-1],a[x]=a[x],a[x-1]
    
    #クエリ2
    if t==2: a=a[0:x-1]+sorted(a[x-1:y],key=int)+a[y:N]
print(' '.join(str(s) for s in a))