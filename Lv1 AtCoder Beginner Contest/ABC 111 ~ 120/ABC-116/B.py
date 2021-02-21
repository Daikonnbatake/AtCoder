s=int(input())
a=[s]
def f(n):
    if n%2==0:return n//2
    else: return (3*n)+1
i=1
while True:
    i+=1
    n=f(a[-1])
    if n in a: break
    a.append(n)
print(i)