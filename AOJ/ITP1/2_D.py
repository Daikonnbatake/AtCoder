W,H,x,y,r=map(int,input().split())
print('Yes'if((0<=x-r and x+r<=W) and (0<=y-r and y+r<=H))else'No')