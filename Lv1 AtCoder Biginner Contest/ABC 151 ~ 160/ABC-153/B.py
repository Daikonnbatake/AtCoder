H,N = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
atk = 0
for i in A:
    atk += i
if atk >= H:
    print("Yes")
else:
    print("No")