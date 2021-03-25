N=int(input())
A=sorted([int(input())for i in range(N)])
a,b=[],[]
x,y=0,0
for i in range(N//2):
    a.extend([A[i],A[N-i-1]])
    b.extend([A[N-i-1],A[i]])

for i in range(N-1):
    x+=abs(a[i]-a[i+1])
    y+=abs(b[i]-b[i+1])

print(a)
print(b)
print(max(x,y))