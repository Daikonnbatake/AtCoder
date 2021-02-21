def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: divisors.append(n//i)
    divisors.sort()
    return divisors
N=int(input())
mem=make_divisors(N)
if len(mem)%2==0: ans=(mem[(len(mem)//2)-1]+mem[(len(mem)//2)])-2
else: ans=(mem[(len(mem)//2)]*2)-2
print(ans)