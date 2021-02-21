w=list(input())
for i in w:
    count=0
    for j in w:
        if i==j:
            count+=1
    if not count%2==0:
        print("No")
        break
if count%2==0:
    print("Yes")