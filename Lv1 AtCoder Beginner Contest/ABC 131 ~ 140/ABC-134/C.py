N=int(input())
A=[]
for i in range(N): A.append(int(input()))
S=sorted(A,key=int)
max1=S[-1]
max2=S[-2]
for i in A:
    if i==max1: print(max2)
    else: print(max1)