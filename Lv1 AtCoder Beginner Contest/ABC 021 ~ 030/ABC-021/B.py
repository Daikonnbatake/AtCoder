N=int(input());a,b=map(int,input().split());K=int(input())
P=list(map(int,input().split()))
P.extend([a,b]); Q=set(P)
print('YES' if len(P)==len(Q) else 'NO')