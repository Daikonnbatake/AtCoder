N=int(input())
S=input()

left = 0
right = 0

for i in range(N):
    if S[i]=='(': right+=1
    else:
        if right == 0: left +=1
        else: right-=1

print('('*left+S+')'*right)