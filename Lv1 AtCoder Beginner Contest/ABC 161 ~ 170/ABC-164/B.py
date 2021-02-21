A,B,C,D=map(int,input().split())
while True:
    if A <= 0 or C <= 0:
        break
    C -= B
    A -= D
print('Yes' if C<=0 else 'No')