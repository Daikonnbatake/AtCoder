n,m=map(int,input().split())
t=abs(n%12*30-m*5.5)
print(min(t,360-t))