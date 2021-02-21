A,B,C=map(int,input().split())
 
if A==B:print('Takahashi' if C else 'Aoki')
else:print('Aoki' if A<B else 'Takahashi')