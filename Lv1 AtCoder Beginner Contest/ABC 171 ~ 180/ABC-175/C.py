X,K,D=map(int,input().split())
if abs(X)<K*D:
    a=X//D
    K-=a
    X-=D*a
    if K%2:
        print(abs(X-D))
    else:
        print(X)
else:
    print(abs(X)-K*D)