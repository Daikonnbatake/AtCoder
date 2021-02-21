A,B,C=map(int,input().split())
count=0
if A < B:
    count+=int(C/A)
    C = int(C/A)
else:
    count+=int(C/B)
    C = int(C/B)
print(count)