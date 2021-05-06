N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=min(B)-max(A)+1
print(0 if a<0 else a)