A=list(input())
B=list(input())
C=list(input())

nxt="a"
while True:
    if nxt=="a":
        if len(A)==0:
            print("A")
            break
        else:
            nxt=A.pop(0)
    if nxt=="b":
        if len(B)==0:
            print("B")
            break
        else:
            nxt=B.pop(0)
    if nxt=="c":
        if len(C)==0:
            print("C")
            break
        else:
            nxt=C.pop(0)