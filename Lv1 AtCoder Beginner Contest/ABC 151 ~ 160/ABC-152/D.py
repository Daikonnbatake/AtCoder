import itertools as it

N=int(input())
l=it.product(['!','!!','!?!','!??!','!???!','!????!'],repeat=2)
ans=0

for a,b in l:
    if a.count('!')+b.count('!')==2:ans+=min(9,N)
    else:
        

print(ans)