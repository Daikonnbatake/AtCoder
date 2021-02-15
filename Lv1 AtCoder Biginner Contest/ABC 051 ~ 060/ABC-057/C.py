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
def F(a,b):return len(str(max(a,b)))

N=int(input())
ans=10**9
for i in md(N):ans=min(ans,F(i,N//i))
print(ans)