N,H=map(int,input().split())
A,B,C,D,E=map(int,input().split())
mem=H-N*E #-なら食事が必要
if 0<mem: print(0)
else:
    if B/A < D/C: print(((abs(mem)//B)+1)*A)
    else: print(((abs(mem)//D)+1)*C)