N,index=int(input()),[]
for x in list(range(1,10)):
    for y in list(range(1,10)):
        if x*y==2025-N:
            index.append(str(x)+" x "+str(y))
index.sort()
for i in index:
    print(i)