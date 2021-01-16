c = [[]for i in range(8)]
pos = []

for i in range(8):
    c[i]=list(input())
    for j in range(8):
        if c[i][j]=='Q':pos.append([i,j])

def FORMAT():return[[0]*8 for i in range(8)]

