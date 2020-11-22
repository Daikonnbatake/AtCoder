N,K = map(int,input().split(" "))
R = list(map(int,input().split(" ")))
R.sort(reverse=True)
r = []
for i in range(K):
    r.append(R[i])
r.sort()
ans = 0
for i in range(K):
    ans = (ans+r[i])/2
print(str(ans)+"\n")