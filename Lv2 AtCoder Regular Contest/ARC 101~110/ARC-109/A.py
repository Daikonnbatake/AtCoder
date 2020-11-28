a,b,x,y=map(int,input().split())
c=abs(a-b)
print(x if a==b else min(2*c*x+x,c*y+x)if a<b else min(2*c*x-x,(c-1)*y+x))