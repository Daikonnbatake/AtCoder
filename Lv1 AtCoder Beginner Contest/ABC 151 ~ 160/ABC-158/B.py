N,A,B=map(int,input().split())
t=N//(A+B)
ans=(t*A)+(min((N%(A+B)),A))
print(ans)