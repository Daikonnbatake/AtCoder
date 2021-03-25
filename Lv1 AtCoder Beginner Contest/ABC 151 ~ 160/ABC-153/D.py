H=int(input())
m=0
ans=0
while 0<H:
    ans+=2**m
    m+=1
    H//=2
print(ans)