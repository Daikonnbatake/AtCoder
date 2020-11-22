N,K=map(int,input().split())
D=list(input().split())
D.insert(0,0)
n=0
while True:
    n+=1
    ok=True
    for i in list(str(n)):
        if i in D:
            ok=False
            break
    if ok and N<=n:
        print(n)
        break