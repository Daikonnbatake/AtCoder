x=input()
if x=="":
    print("YES")
    exit()
else:
    i=0
    while i < len(x):
        if not x[i] in ["o","k","u"]:
            if i+1<=len(x):
                if x[i:i+2] == "ch":
                    i+=1
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
        i+=1
    print("YES")
