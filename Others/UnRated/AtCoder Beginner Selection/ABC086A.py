a,b = map(int, input().split())

m = a * b
ans = m % 2

if ans==0:
    print('Even')

else:
    print('Odd')