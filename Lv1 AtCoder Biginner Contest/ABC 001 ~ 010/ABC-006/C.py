N,M=map(int,input().split())

for c in range(N+1):
    
    a = -M + 3*N + c
    b = M - 2*N -2*c
    
    if min(a,b,c) >= 0:
        print(a, b, c)
        exit()

print(-1,-1,-1)