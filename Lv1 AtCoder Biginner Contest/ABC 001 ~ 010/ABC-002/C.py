inp = list(map(int,input().split(" ")))
X = []
Y = []
for i in range(3):
    X.append(inp[i*2])
    Y.append(inp[i*2+1])
oX = X[0]
oY = Y[0]
a = X[1] - oX
b = Y[1] - oY
c = X[2] - oX
d = Y[2] - oY
print(str(abs(a*d-b*c)/2))