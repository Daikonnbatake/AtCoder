N,a=int(input()),''
while 0<N:N-=1;a+=chr(97+N%26);N//=26
print(a[::-1])