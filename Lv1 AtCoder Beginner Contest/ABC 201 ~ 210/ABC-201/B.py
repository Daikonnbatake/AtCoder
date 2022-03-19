N=int(input())
ST=sorted([list(input().split()) for i in range(N)], key=lambda x: -int(x[1]))
print(ST[1][0])