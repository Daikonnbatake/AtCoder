A,B=map(int,input().split())
for i in range(10000):
    if int((i+1)*8/100) == A and int((i+1)*10/100) == B:
        print(i+1)
        exit()
print(-1)