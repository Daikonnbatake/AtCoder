N=int(input())
v=list(map(int,input().split()))
v=sorted(v,key=int)
def fusion():
    if len(v)==1:
        return v[0]
    else:
        v.insert(0,(v.pop(0)+v.pop(0))/2)
        v.sort(key=float)
        return fusion()
print(fusion())