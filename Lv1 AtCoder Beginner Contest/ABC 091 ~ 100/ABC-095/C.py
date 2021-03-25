A,B,C,X,Y=map(int,input().split())
ans=10**10
for i in range(max(X,Y)+1):ans=min(ans,(C*i*2)+(max(0,X-i)*A)+(max(0,Y-i)*B))
print(ans)