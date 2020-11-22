K=int(input())
A,B=map(int,input().split())
for i in range(1000):
    if (i+1)%K==0 and (A <= (i+1) and (i+1) <= B) :
        print('OK')
        exit()
print('NG')