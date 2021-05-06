R,X,Y=map(int,input().split())
d=(X**2 + Y**2)**0.5
if d==R:print(1)
elif d<=R+R:print(2)
else:print(int(-(-d//R)))