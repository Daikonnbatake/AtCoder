X,Y,A,B=map(int,input().split())
y=0
while A*X<min(B,Y):
    X*=A
    y+=1
print(y+((Y-X-1)//B))