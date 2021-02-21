N=int(input())
A,ans=[int(input()) for i in range(N)],[0,0]
for i in A:
    if ans[0] < i:
        ans[1],ans[0] = ans[0],i
    elif ans[1] < i and i < ans[0]:
        ans[1] = i
print(ans[1])