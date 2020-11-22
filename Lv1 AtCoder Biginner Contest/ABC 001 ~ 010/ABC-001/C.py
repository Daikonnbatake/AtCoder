from decimal import Decimal as d
Deg, Dis = map(int, input().split())
a = 'N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW N'.split()
b = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326, 2000]

x = a[(Deg*10 + 1125) // 2250]
y = 0

for i in range(13):
    if  (d(str(Dis))/d('6.0')).quantize(0, rounding='ROUND_HALF_UP') <= b[i]:
        y = i
        break

print(x if y else 'C', y)