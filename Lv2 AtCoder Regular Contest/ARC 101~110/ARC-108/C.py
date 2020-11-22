from collections import deque

N,s=int(input()),list(input())

stack = deque()
for i in range(3):stack.append('0')
ans = N

for i in s:
    stack.append(i)

    if stack[-3]+stack[-2]+stack[-1] == 'fox':
        for i in range(3):
            stack.pop()
        ans-=3
print(ans)