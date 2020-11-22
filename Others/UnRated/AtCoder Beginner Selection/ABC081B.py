N = int(input())
A = list(map(int, input().split()))

ans = 0
flag = True

while flag == True:
    for i in range(N):
        if (A[i] % 2) == 1:
            flag = False
        else:
            A[i] /= 2
    if flag == True:
        ans += 1

print(ans)