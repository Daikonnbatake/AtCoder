import statistics as s
N=int(input())
A=list(map(int,input().split()))
A=[A[i]-i-1 for i in range(N)]
m=int(s.median(A))
print(sum([abs(i-m)for i in A]))