A=int(input())
ans=[1,1]
for i in range(100):
    for j in range(100):
        if (i+1)+(j+1)==A:
            ans = [i+1,j+1] if (ans[0]*ans[1] < (i+1)*(j+1)) else ans
print(ans[0]*ans[1])