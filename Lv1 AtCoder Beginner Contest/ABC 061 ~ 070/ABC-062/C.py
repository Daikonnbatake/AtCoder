H,W=map(int,input().split())

l,r=1,H*W
while l<r:
    mid=(l+r)//2
    m=mid*3
    if m<r:r=mid
    elif l<m:l=mid

print(l,r)