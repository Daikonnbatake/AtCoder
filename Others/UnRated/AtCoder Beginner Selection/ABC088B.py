N = int(input())
a = list(map(int, input().split()))

a.sort()

alice, bob = 0,0

for i in range(N):
    if i%2 == 0:
        alice += a[N-i-1]
    else:
        bob += a[N-i-1]

print(alice - bob)