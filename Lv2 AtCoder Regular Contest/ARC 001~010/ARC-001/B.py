A,B = map(int,input().split())
C = abs(A-B)

ans = 0

while True:
    if C==0: break
    a = [abs(C-10),abs(C-5),abs(C-1)]
    b = a.index(min(a))
    if b==2:C = abs(C-1)
    elif b==1:C = abs(C-5)
    else: C = abs(C-10)
    ans+=1

print(ans)