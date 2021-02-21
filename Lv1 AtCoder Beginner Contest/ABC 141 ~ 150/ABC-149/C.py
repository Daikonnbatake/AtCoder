import math
X=int(input())
ans = X
def prime(n):
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

while True:
    if prime(ans):
        break
    ans += 1
print(ans)