N,X,T=map(int,input().split())
print(((N//X)+(1 if N%X else 0))*T)