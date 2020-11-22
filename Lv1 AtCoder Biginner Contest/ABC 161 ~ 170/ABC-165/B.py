X=int(input())
n=100
y=0
while n<X:
    y+=1
    n+=int((n*0.01))
print(y)