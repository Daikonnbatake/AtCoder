A,R,N=map(int,input().split())
if R*(N-1)>10**9: print('large')
else:
    if (R**(N-1))*A <= 10**9: print((R**(N-1))*A)
    else: print('large')