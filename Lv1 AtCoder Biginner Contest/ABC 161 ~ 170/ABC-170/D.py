import math # ←これを忘れないように！

def prime(n):
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=0
o=True if 1 in A else False
for i in A:
    if prime(i) and o: ans+=1
    else:
        for j in A:
            i%j
print(ans)