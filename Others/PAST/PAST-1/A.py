S=list(input())
c=list("0123456789")
r=""
for i in S:
    if not i in c:
        print("error")
        exit()
    else:
        r=r+i
print(int(r)*2)