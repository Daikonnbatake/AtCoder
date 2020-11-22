N = int(input())

a = [0]*290

for i in range(N):

    S, E = input().split('-')
    S = int(S[:2])*12 + (int(S[-2:])//5)
    E = int(E[:2])*12 + (1 if int(E[-2:]) % 5 else 0) + int(E[-2:])//5

    a[S + 1] += 1
    a[E + 1] -= 1

s, e = '0000', '0000'
rain = False

for i in range(1,290):

    a[i] = a[i - 1]+a[i]

    h, m, = str((i-1)//12), str((i - 1)%12*5)
    h = h if 1 < len(h) else '0' + h
    m = m if 1 < len(m) else '0' + m

    if rain != (0 < a[i]):
        if rain:
            e = h + m
            print(s + '-' + e)

        else:
            s = h + m

    rain = 0 < a[i]