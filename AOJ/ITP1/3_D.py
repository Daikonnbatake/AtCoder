def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: divisors.append(n//i)
    divisors.sort()
    return divisors

a,b,c=map(int,input().split())
ans=0
for i in make_divisors(c):
    if a<=i and i<=b:ans+=1
print(ans)