N,K,X,Y=int(input()),int(input()),int(input()),int(input())
if K < N:
    print(K*X+(N-K)*Y)
else:
    print(N*X)