N = int(input())
X, Y = 0, 0
flag = True

for i in range(N):
    t, x, y = map(int,input().split())
    if t < (x + y) or (t % 2) != ((x + y) % 2):
        flag = False
    X, Y = x, y

if flag == True:
    print('Yes')

else:
    print('No')