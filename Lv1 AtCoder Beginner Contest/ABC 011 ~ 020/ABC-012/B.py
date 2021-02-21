N=int(input())
H,M,S=str(int(N/3600)),str(int(N/60)%60),str(N%60)
print((H if len(H)==2 else "0" + H)+":"+(M if len(M)==2 else "0" + M)+":"+(S if len(S)==2 else "0" + S))