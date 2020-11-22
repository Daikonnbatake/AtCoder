N=int(input())
A=list(map(int,input().split()))
A.sort(key=int)
l=0
for i in range(N):
    c=0
    while l < len(A) and A[l] == i+1:
        l+=1
        c+=1
    print(c)