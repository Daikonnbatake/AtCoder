N,M=map(int,input().split())
s,c=[0]*M,[0]*M
for i in range(M):
    s[i],c[i] = map(int,input().split())
for i in range(10**N):
    if len(str(i)) != N:
        pass
    else:
        num=list(str(i))
        ok = True
        for j in range(M):
            if num[s[j]-1] != str(c[j]):
                ok = False
        if ok:
            print(i)
            exit()
print(-1)