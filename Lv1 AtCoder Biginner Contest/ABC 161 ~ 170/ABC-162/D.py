import math
N,K=map(int,input().split())
print(math.factorial(N+1)//math.factorial((N+1)-K)%(10**9+7))