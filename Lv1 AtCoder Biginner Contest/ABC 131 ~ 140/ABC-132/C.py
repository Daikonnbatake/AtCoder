N=int(input())
d=sorted(list(map(int,input().split())),key=int)
print(d[(N//2)]-d[(N//2)-1])