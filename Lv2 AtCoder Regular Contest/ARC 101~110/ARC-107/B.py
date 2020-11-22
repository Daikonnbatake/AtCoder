N,K=map(int,input().split())
A=2
ans=0
for i in range(N):
    B=A-K
    ans+=(A-1)*(B-1)
    A+=1
print(ans*2)

#10314607400
#8042948200