sx,sy=map(int,input().split())
gx,gy=map(int,input().split())

sx,sy,gx,gy=0,0,abs(sx-gx),abs(sy-gy)

if sx==gx and sy==gy:print(0)
if 