N=int(input())
mem=0
for i in range(N):
    A=int(input())
    if i!=0:
        if mem==A: print('stay')
        elif mem>A: print('down '+str(mem-A))
        elif mem<A: print('up '+str(A-mem))
    mem=A