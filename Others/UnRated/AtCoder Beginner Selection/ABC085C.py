N,Y = map(int, input().split())

a = Y // 10000
Y -= a * 10000

b = Y // 5000
Y -= b * 5000

c = Y // 1000
Y -= c * 1000

if (a + b + c) <= N:
    print(a,b,c)

else:
    print(-1, -1, -1)