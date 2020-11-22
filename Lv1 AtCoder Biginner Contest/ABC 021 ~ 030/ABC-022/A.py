N,S,T=map(int,input().split())
W=int(input())
count= 1 if S <= W and W <= T else 0
for i in range(N-1):
    A=int(input())
    W+=A
    if S <= W and W <= T:
        count+=1
print(count)