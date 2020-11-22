H,W=map(int,input().split())
print(int((H*W)/2) if (H*W)%2==0 else int(((H*W)+1)/2))