N,S=int(input()),input()
a,b='',''
if N%2==0:
    for i in range(int(N/2)):
        a = a+S[i]
        b = S[len(S)-(i+1)]+b
    print('Yes' if a==b else 'No')
else:
    print('No')