mod=10**9+7
def f(n,a,b):
    global mod
    if n<a+b:return 0
    else:
        x=n-a+1
        y=n-b+1
        return ((x**2)*(y**2)-(y**2)*(a**2)-)%mod
T=int(input())
for i in range(T):
    n,a,b=map(int,input().split())
    if a>b:a,b=b,a
    print(f(n,a,b))