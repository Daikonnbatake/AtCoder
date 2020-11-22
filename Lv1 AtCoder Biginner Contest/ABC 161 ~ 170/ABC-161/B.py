N,M=map(int,input().split())
A=list(map(int,input().split()))
S=sum(A)
c=0

for i in A:
    if (1/(M*4)) <= (i/S):
        c+=1
print("Yes" if M<=c else "No")