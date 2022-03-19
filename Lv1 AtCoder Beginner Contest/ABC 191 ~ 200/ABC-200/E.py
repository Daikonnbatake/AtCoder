N,K=map(int,input().split())
a=(K-1)//3 # 大周期
b=(K-1)%3 # 中周期
print(a+b+3)