A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for i in range(A+1):
    for j in range(B+1):
        memo = ((X - (i * 500) - (j * 100)) // 50)
        if (0 <= memo) and (memo <= C) :
            ans += 1

print(ans)