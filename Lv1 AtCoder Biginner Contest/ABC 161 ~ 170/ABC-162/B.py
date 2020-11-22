N=int(input())
count = 0
for i in range(N):
    if not(((i+1)%3 == 0)or((i+1)%5 == 0)):
        count += i+1
print(count)