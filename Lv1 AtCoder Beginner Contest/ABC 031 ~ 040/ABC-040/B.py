n=int(input())
ans=10**5
for i in range(1,n+1):
    x=n//i;y=n//x;p=n-(x*y)
    ans=min(ans,p+abs(x-y))
print(ans)