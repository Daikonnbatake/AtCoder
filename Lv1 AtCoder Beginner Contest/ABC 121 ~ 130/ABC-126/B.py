S=input()
A,B=int(S[:2]),int(S[2:])

def f(A,B):
    if 0<A and A<=12 and 0<B and B<=12: return 'AMBIGUOUS'
    if 0<A and A<=12: return 'MMYY'
    if 0<B and B<=12: return 'YYMM'
    return 'NA'

print(f(A,B))