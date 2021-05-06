n,k=map(int,input().split())
s=[int(input()) for i in range(n)]
if 0 in s:print(n);exit()
if k<min(s):print(0);exit()
ans,r,cur=0,0,1
for l in range(n):
    while r < n and cur * s[r] <= k:
        cur *= s[r]
        r += 1
    ans = max(ans, r-l)
    if l == r:
        r += 1
    cur //= s[l]
print(ans)