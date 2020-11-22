n = int(input())
a = [0]*max(n,3)

a[0], a[1], a[2] = 0, 0, 1

for i in range(3,n):
    a[i] = (a[i-3] + a[i-2] + a[i-1]) % 10007

print(a[n-1])