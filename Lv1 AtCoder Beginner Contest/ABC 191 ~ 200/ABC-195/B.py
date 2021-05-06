import math as m
A,B,W=map(int,input().split())
h=m.floor(1000*W/A)
l=m.ceil(1000*W/B)
if l>h:print('UNSATISFIABLE')
else:print(l,h)