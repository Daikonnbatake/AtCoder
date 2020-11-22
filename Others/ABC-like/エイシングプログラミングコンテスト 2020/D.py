
def popcount(n):return bin(n).count('1')
def f(n):
    r=0
    while 0<n:
        n=n%popcount(n)
        r+=1
    return r

N=int(input())
X='0b'+input()

for i in range(X):
    