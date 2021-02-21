n=int(input())
B=[105]*(310)
B[0]=0
for i in range(3):
  B[int(input())]=1000
for i in range(n):
  for j in range(3):
    if B[i]==1000:
      continue
    if B[i+j+1]!=1000:
      B[i+j+1]=min(B[i+j+1],B[i]+1)
print('NO'if B[n]>100 else'YES')