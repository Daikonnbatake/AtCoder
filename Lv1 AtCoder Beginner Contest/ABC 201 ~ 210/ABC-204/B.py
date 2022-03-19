N=int(input())
ans=0
for i in map(int,input().split()):ans += max(0, i-10)
print(ans)