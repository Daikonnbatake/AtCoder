X,Y=map(int,input().split())
if X*4<Y: print('No')
elif X*2>Y: print('No')
else: print('Yes' if (Y%4)%2==0 else 'No')