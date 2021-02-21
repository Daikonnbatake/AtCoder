import math
def md(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def p(n):
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0: return False
    return True

A,B=map(int,input().split())
div = set(md(A)) & set(md(B))
ans=0

for i in div:
    if p(i):ans+=1

print(ans+1)