def g(n,mod):return pow(n,mod-2,mod)

#割り算特化拡張
def modiv(a,b,mod):return a*pow(b,mod-2,mod)%mod