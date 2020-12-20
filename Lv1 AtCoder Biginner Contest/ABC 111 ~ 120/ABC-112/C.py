N=int(input())
p=[list(map(int,input().split()))for i in range(N)]

for Cy in range(101):
    for Cx in range(101):
        
        H = -1

        for x,y,h in p:
            if 0<h:
                tmp = h + abs(Cx-x) + abs(Cy-y)
                if H == -1: H = tmp
                elif H != tmp:
                    H = -2
                    break
        
        if H == -2: continue

        for x,y,h in p:
            if h == 0:
                dist = abs(Cx-x) + abs(Cy-y)
                if H > dist:
                    H = -2
                    break
        
        if H == -2: continue

        print(Cx,Cy,H)