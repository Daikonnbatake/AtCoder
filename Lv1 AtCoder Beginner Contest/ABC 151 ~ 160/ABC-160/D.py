N,X,Y=map(int,input().split())

k=[0]*(N-1)

for i in range(N-1):
    for j in range(i+1,N):
        if i<=X and Y<=j:
            pass
        else: k[j-i-1] +=1

print(k)