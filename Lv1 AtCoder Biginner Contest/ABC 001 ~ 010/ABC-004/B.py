O = ["","","",""]
for i in range(4):
    inp = input().split(" ")
    stack = ""
    for j in range(4):
        stack = stack + inp[-(j+1)]+" "
    O[-(i+1)] = stack
for i in range(4):
    if i == 3:
        print(O[i]+"\n")
    else:
        print(O[i])