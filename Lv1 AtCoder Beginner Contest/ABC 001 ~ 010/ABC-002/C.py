x,y,a,b,c,d = list(map(int,input().split()))
print(abs((a-x)*(d-y) - (b-y)*(c-x))/2)