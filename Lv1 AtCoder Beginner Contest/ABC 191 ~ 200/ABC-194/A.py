A,B=map(int,input().split())
S=A+B
if 15<=S and 8<=B:print(1)
elif 10<=S and 3<=B:print(2)
elif 3<=B:print(3)
else:print(4)