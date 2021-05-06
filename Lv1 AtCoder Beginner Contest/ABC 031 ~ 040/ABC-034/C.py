def f(n,mod):
    ret=1
    for i in range(1,n+1):ret=ret*i%mod
    return ret

def m(a,b,mod):return a*pow(b,mod-2,mod)%mod

W,H=map(int,input().split())
mod=10**9+7
print(m(f(H+W-2,mod),f(H-1,mod)*f(W-1,mod),mod))

#print(f(H+W-2,mod) * g(f(H-1,mod)*f(W-1,mod),mod) % mod)