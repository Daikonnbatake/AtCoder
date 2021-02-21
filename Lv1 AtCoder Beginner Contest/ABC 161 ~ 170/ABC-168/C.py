import math
A,B,H,M=map(int,input().split())
H=((H+(M/60))/12)*360; M=(M/60)*360
C=abs(H-M)
C=math.cos(math.radians(C))
print(math.sqrt((A**2)+(B**2)+(-2*A*B*C)))